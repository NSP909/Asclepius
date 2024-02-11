import { useState, useEffect } from "react";
import axios from "axios";

const SearchPredict = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [sql, setSql] = useState('');

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

      // Handle search results or other actions here
    } catch (error) {
      console.error('Error searching:', error);
    }
  };

  const onSubmit = async () => {
    try {
        console.log('hello')
        const response = await axios.post('http://104.248.110.113:5000/performquery', {query: sql});
        console.log('Search results:', response.data);
        } catch (error) {
        console.error('Error searching:', error);
      }
  }

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
        
    </div>
    
  );
};

export default SearchPredict;