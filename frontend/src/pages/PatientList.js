// PatientsList.js
import Header from "./components/Header";
import React, { useState, useEffect } from "react";
import getWindowDimensions from "./Window";
import FullReport from "./FullReport";
import Summary from "./Summary";
import Prediction from "./Prediction";

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

    FullReport(userId)
      .then((data) => {
        console.log("Full Report Data:", data);
      })
      .catch((error) => {
        console.error("Error fetching Full Report:", error);
      });
  };

  const handleSummary = (userId) => {
    console.log(`Fetching Summary for user ID: ${userId}`);

    Summary(userId)
      .then((data) => {
        console.log("Full Report Data:", data);
      })
      .catch((error) => {
        console.error("Error fetching Full Report:", error);
      });
  };

  const handlePredictions = (userId) => {
    console.log(`Fetching Predictions for user ID: ${userId}`);

    Prediction(userId)
      .then((data) => {
        console.log("Full Report Data:", data);
      })
      .catch((error) => {
        console.error("Error fetching Full Report:", error);
      });
  };
//  return(
//   <div className="flex flex-col w-full h-screen overflow-y-hidden items-center">
//     <Header />
//     <div className="text-primary h-screen p-4 w-screen font-karla">
//       <h1 className="text-3xl font-bold mb-4">Patient List</h1>
//       <div
//         className="flex flex-col h-full w-auto items-center"
//         style={{ overflow: "auto", maxHeight: getWindowDimensions().height }}
//       >
//         <div class="bg-white overflow-auto">
//           <table className="min-w-full bg-white">
//             <thead className="bg-gray-800 text-white">
//               <tr>
//               <th class="w-1/3 py-3 px-4 uppercase font-semibold text-sm text-left">ID</th>
//               <th class="w-1/2 text-left py-3 px-4 uppercase font-semibold text-sm">Name</th>
//               <th class="text-left py-3 px-4 uppercase font-semibold text-sm">Date Of Birth</th>
//               </tr>
//             </thead>
//             <tbody>
//               {patientsData.map((patient) => (
//                 <tr key={patient.user_id}>
//                   <td>{patient.user_id}</td>
//                   <td>{patient.fullname}</td>
//                   <td>
//                     <input
//                       type="radio"
//                       name="selectedPatient"
//                       value={patient.user_id}
//                       // onChange={() => handlePatientSelection(patient.user_id)}
//                     />
//                   </td>
//                 </tr>
//               ))}
//             </tbody>
//           </table>
//         </div>
//       </div>
//     </div>
//   </div>
//  )
  return (
    <div className="flex flex-col w-full h-screen overflow-y-hidden items-center">
      <Header />
      <div className="text-primary h-screen p-4 w-screen font-karla">
        <h1 className="text-3xl font-bold mb-4">Patient List</h1>
        <div
          className="flex flex-col h-full w-auto items-center"
          style={{ overflow: "auto", maxHeight: getWindowDimensions().height }}
        >
          {patientsData.map((patient) => (
            <div
              key={patient.user_id}
              className="bg-white text-black p-4 mb-4  flex-grow w-1/2 md-2/3 rounded items-center justify-center"
            >
              <strong>ID:</strong> {patient.user_id}, <strong>Name:</strong>{" "}
              {patient.username}
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
    </div>
  );
};

export default PatientsList;

const TableView = ()=> {
  
};
