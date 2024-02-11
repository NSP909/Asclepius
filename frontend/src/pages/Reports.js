// Reports.js
import Header from "./components/Header";
import React, { useState,useEffect } from "react";
import { useParams } from 'react-router-dom';
import ReportsTable from "./ReportsTable";
import axios from "axios";

const Reports = ({userID}) => {
  // Sample JSON data
  const { id } = useParams();
  const reportId = parseInt(id);
  const [jsondata, setData] = useState(null);

  // const jsonData = {
  //   "notes": [{"note":"wefefw", "note_date":"fwefw"}],
  //       "medicine": [{"med_name":"lmo", "med_dosage":"wefwef", "med_frequency":"edfwef", "med_date":"wefwef"}],
  //       "vaccine": [{"vac_name":"wrrf", "vac_date":"fewfwe"}],
  //       "lab_result": [{"lab_result":"wefwed", "lab_date":"wefwef"}],
  //       "surgeries": [{"surgery":"wefwef", "surgery_date":"wewd"}],
  //       "emergencies": [{"emergency_name":"wedwed", "emergency_date":"wefwf"}],
  //       "vitals": [{"vital_name":"rgeg", "vital_value":"wfwfe", "vital_date":"rswerg"}],
  //       "diagnosis": [{"diagnosis":"eee", "diag_date":"eeee"}],
  //       "symptoms": [{"symptom":"wrf", "symptom_date":"eerer"}]
  // };
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.post('http://104.248.110.113:5000/getentirehistory', { user_id: reportId });
        console.log(response.data)
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="w-screen">
      <Header/>     
      {jsondata && <ReportsTable jsonData={jsondata} />}
    </div>
  );
};

export default Reports;