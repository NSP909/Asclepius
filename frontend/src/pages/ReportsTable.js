import React from "react";
import getWindowDimensions from "./Window";
  
  

const ReportsTable = ({ jsonData }) => {
  // Function to create and return a table for a specific category
  const createAndReturnTable = (category, data) => {
    // Start building the table HTML
    var tableHTML = `<div class="mb-8 bg-blue-500 text-white rounded-lg p-4">
      <h2 class="text-2xl font-bold mb-4">${category} Table</h2>
      <table class="min-w-full bg-white shadow-md rounded-md mb-4">
        <thead>
          <tr class="bg-blue-500 text-white font-semibold">`;
    // Table headers
    Object.keys(data[0]).forEach((header) => {
      tableHTML += `<th class="py-2 px-4 border">${header}</th>`;
    });
    tableHTML += `</tr>
        </thead>
        <tbody>`;
    // Iterate over JSON data and create table rows
    data.forEach((item, index) => {
      tableHTML += `<tr class="${index % 2 === 0 ? 'bg-blue-100' : 'bg-white'} text-blue-900">`;
      Object.values(item).forEach((value) => {
        tableHTML += `<td class="py-2 px-4 border">${value}</td>`;
      });
      tableHTML += `</tr>`;
    });
    // End the table HTML
    tableHTML += `</tbody></table></div>`;
    // Wrap the table in a div and return the entire HTML string
    return <div dangerouslySetInnerHTML={{ __html: tableHTML }} />;
  };

  return (
    <div className="flex flex-wrap justify-center p-4 " style={{ overflow: 'auto', maxHeight: getWindowDimensions().height }}>
      <div className="flex flex-wrap w-full md:w-1/2">
        <div className="w-full">{createAndReturnTable("Notes", jsonData.notes)}</div>
        <div className="w-full">{createAndReturnTable("Medicine", jsonData.medicine)}</div>
      </div>
      <div className="flex flex-wrap w-full md:w-1/2">
        <div className="w-full">{createAndReturnTable("Vaccine", jsonData.vaccine)}</div>
        <div className="w-full">{createAndReturnTable("Lab Results", jsonData.lab_result)}</div>
      </div>
      <div className="flex flex-wrap w-full md:w-1/2">
        <div className="w-full">{createAndReturnTable("Surgeries", jsonData.surgeries)}</div>
        <div className="w-full">{createAndReturnTable("Emergencies", jsonData.emergencies)}</div>
      </div>
      <div className="flex flex-wrap w-full md:w-1/2">
        <div className="w-full">{createAndReturnTable("Vitals", jsonData.vitals)}</div>
        <div className="w-full">{createAndReturnTable("Diagnosis", jsonData.diagnosis)}</div>
      </div>
      <div className="w-full md:w-full">{createAndReturnTable("Symptoms", jsonData.symptoms)}</div>
    </div>
  );
};



export default ReportsTable;