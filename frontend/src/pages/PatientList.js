// PatientsList.js

import React, { useState, useEffect } from "react";
import getWindowDimensions from "./Window";
const PatientsList = () => {
  const [patientsData, setPatientsData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://104.248.110.113:5000/getpatients");
        const data = await response.json();
        setPatientsData(data);
      } catch (error) {
        console.error("Error fetching patient data:", error);
      }
    };

    fetchData();
  }, []);

  const handleFullReport = (userId) => {
    console.log(`Fetching Full Report for user ID: ${userId}`);
    // Implement the logic for fetching the Full Report here
  };

  const handleSummary = (userId) => {
    console.log(`Fetching Summary for user ID: ${userId}`);
    // Implement the logic for fetching the Summary here
  };

  const handlePredictions = (userId) => {
    console.log(`Fetching Predictions for user ID: ${userId}`);
    // Implement the logic for fetching Predictions here
  };

  return (
    <div className="bg-blue-500 text-white h-screen p-4">
      <h1 className="text-2xl font-bold mb-4">Patient List</h1>
      <div className="flex flex-col h-full w-screen items-center" style={{ overflow: 'auto', maxHeight: getWindowDimensions().height }}>
        {patientsData.map(patient => (
          <div
            key={patient.user_id}
            className="bg-white text-black p-4 mb-4  flex-grow w-1/2 md-2/3 rounded items-center justify-center"
          >
            <strong>ID:</strong> {patient.user_id}, <strong>Name:</strong> {patient.username}
            <div className="mt-2">
              <button
                className="bg-green-500 text-white px-4 py-2 mr-2 rounded"
                onClick={() => handleFullReport(patient.user_id)}
              >
                Full Report
              </button>
              <button
                className="bg-blue-500 text-white px-4 py-2 mr-2 rounded"
                onClick={() => handleSummary(patient.user_id)}
              >
                Summary
              </button>
              <button
                className="bg-purple-500 text-white px-4 py-2 rounded"
                onClick={() => handlePredictions(patient.user_id)}
              >
                Predictions
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default PatientsList;
