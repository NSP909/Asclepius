// Reports.js
import Header from "./components/Header";
import React from "react";
import ReportsTable from "./ReportsTable";

const Reports = () => {
  // Sample JSON data
  const jsonData = {
    "notes": [{"note":"wefefw", "note_date":"fwefw"}],
        "medicine": [{"med_name":"lmo", "med_dosage":"wefwef", "med_frequency":"edfwef", "med_date":"wefwef"}],
        "vaccine": [{"vac_name":"wrrf", "vac_date":"fewfwe"}],
        "lab_result": [{"lab_result":"wefwed", "lab_date":"wefwef"}],
        "surgeries": [{"surgery":"wefwef", "surgery_date":"wewd"}],
        "emergencies": [{"emergency_name":"wedwed", "emergency_date":"wefwf"}],
        "vitals": [{"vital_name":"rgeg", "vital_value":"wfwfe", "vital_date":"rswerg"}],
        "diagnosis": [{"diagnosis":"eee", "diag_date":"eeee"}],
        "symptoms": [{"symptom":"wrf", "symptom_date":"eerer"}]
  };

  return (
    <div className="w-screen">
      <Header/>     
      <ReportsTable jsonData={jsonData} />
    </div>
  );
};

export default Reports;