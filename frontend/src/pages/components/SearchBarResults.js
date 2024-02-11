import React, { useState, useEffect } from "react";
import axios from "axios";

const SearchPredict = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [sql, setSql] = useState('');
  const [results, setResults] = useState([]);

  const handleChange = (event) => {
    setSearchQuery(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      // Make Axios POST request with searchQuery data
      const response = await axios.post('http://104.248.110.113:5000/convertNLPtoSQL', { text: searchQuery });
      console.log('Search results:', response.data);
      setSql(response.data.query);

    } catch (error) {
      console.error('Error searching:', error);
    }
  };

  const onSubmit = async () => {
    try {
      console.log('hello')
      const response = await axios.post('http://104.248.110.113:5000/performquery', {query: sql});
      console.log('Search results:', response.data.result);
      setResults(response.data.result);
    } catch (error) {
      console.error('Error searching:', error);
    }
  }

  const headers = results.length > 0 ? Object.keys(results[0]) : [];

  return (
  <div className="flex flex-col items-center gap-10">
    <form onSubmit={handleSubmit} className="flex items-center border rounded-md shadow-md overflow-hidden">
      <input
        type="text"
        value={searchQuery}
        onChange={handleChange}
        placeholder="Search..."
        className="py-2 px-4 w-[30vw] outline-none h-[8vh]"
      />
      <button type="submit" className="bg-headerColor hover:bg-blue-600 text-white py-2 px-4 h-[8vh]">
        Search
      </button>
    </form>
    {sql && <div className=" bg-gray-200 h-[8vh] max-h-[16vh] w-[60vw] overflow-y-auto border-dashed border-2 border-gray-900 p-4">
      <code>{sql}</code>
    </div>}
    {sql && <button type="submit" onClick={onSubmit} className="bg-headerColor hover:bg-gray-600 text-white py-2 px-4 rounded-full">
      <i class="fas fa-check"></i>
    </button>}
    <div style={{ 
      maxHeight: '300px', // adjust as needed
      overflowY: 'auto'
    }}>
      <div className = '' style={{ 
        display: 'table', 
        boxShadow: '0px 0px 8px 2px rgba(0,0,0,0.1)', 
        borderRadius: '10px', 
        overflow: 'hidden' 
      }}>
        <div style={{ display: 'table-header-group' }}>
          <div style={{ display: 'table-row' }}>
            {results.length > 0 && <div style={{ 
              display: 'table-cell', 
              backgroundColor: '#f2f2f2', 
              padding: '10px', 
              margin: '5px', 
              borderRadius: '10px',
              fontWeight: 'bold',
              fontSize: '20px'
            }}>
              Serial
            </div>}
            {headers.map((header, index) => (
              <div key={index} style={{ 
                display: 'table-cell', 
                backgroundColor: '#f2f2f2', 
                padding: '10px', 
                margin: '5px', 
                borderRadius: '10px' ,
                fontWeight: 'bold',
                fontSize: '20px'
              }}>
                {header}
              </div>
            ))}
          </div>
        </div>
        <div style={{ display: 'table-row-group' }}>
          {results.map((result, index) => (
            <div key={index} style={{ display: 'table-row' }}>
              {results.length > 0 && <div style={{ 
                display: 'table-cell', 
                padding: '10px', 
                margin: '5px', 
                borderRadius: '10px' 
              }}>
                {index + 1}
              </div>}
              {headers.map((header, index) => (
                <div key={index} style={{ 
                  display: 'table-cell', 
                  padding: '10px', 
                  margin: '5px', 
                  borderRadius: '10px' 
                }}>
                  {result[header]}
                </div>
              ))}
            </div>
          ))}
        </div>
      </div>
    </div>
  </div>
);
};

export default SearchPredict;