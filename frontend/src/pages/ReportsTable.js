import React from "react";
import getWindowDimensions from "./Window";
  
  

const ReportsTable = ({ jsonData }) => {
  // Function to create and return a table for a specific category
  const createAndReturnTable = (category, data) => {
    // Start building the table HTML
    var tableHTML = `<div class="mb-8 bg-gray-200 text-[#212936] rounded-sm p-4 border-dashed border-gray-400 border-2">
      <h2 class="text-base font-bold mb-4">${category}</h2>
      <table class="min-w-full bg-white shadow-md rounded-md mb-4">
        <thead>
          <tr class="bg-headerColor text-white font-semibold">`;
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
    <div className="grid grid-cols-2 gap-4 p-4" style={{ overflow: 'auto', maxHeight: getWindowDimensions().height }}>
    <div>{createAndReturnTable("Clinical Notes", jsonData.notes)}</div>
    <div>{createAndReturnTable("Medicine", jsonData.medicine)}</div>
    <div>{createAndReturnTable("Vaccine", jsonData.vaccine)}</div>
    <div>{createAndReturnTable("Lab Results", jsonData.lab_result)}</div>
    <div>{createAndReturnTable("Surgeries", jsonData.surgeries)}</div>
    <div>{createAndReturnTable("Emergencies", jsonData.emergencies)}</div>
    <div>{createAndReturnTable("Vitals", jsonData.vitals)}</div>
    <div>{createAndReturnTable("Diagnosis", jsonData.diagnosis)}</div>
    <div className="col-span-2">{createAndReturnTable("Symptoms", jsonData.symptoms)}</div>
  </div>
  );
};



export default ReportsTable;