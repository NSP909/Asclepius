import { Upload } from "lucide-react";
import { Link, Routes, Route } from "react-router-dom";
import React from "react";
import AddReport from "./AddReport";
import DashBoard from "./DashBoard";
import Reports from "./Reports";
import PatientsList from "./PatientList";

const Main = () => {
  return (
    <div className="flex w-full h-screen overflow-y-hidden">
      <Sidebar />
      {/* this is the upload file page */}
      <Routes>
        <Route path="/add" element={<AddReport />} />
        <Route path="/" element={<DashBoard />} />
        <Route path="/reports" element={<Reports />} />
        <Route path="/Patients" element={<PatientsList />} />
      </Routes>
    </div>
  );
};

const Sidebar = () => {
  return (
    <aside className="pt-4 bg-sidebar h-screen w-64 hidden sm:block shadow-xl">
      <div className="p-3">
        <a
          href="#"
          className="text-white text-3xl font-semibold uppercase hover:text-gray-300"
        >
          DuoDoc
        </a>
        <Link to="/d/add">
          <button className=" mt-10 w-full bg-white cta-btn font-semibold py-2 rounded-br-lg rounded-bl-lg rounded-tr-lg shadow-lg hover:shadow-xl hover:bg-gray-300 flex items-center justify-center">
            <i className="fas fa-plus mr-3"></i> Add Report
          </button>
        </Link>
      </div>
      <nav className="text-white text-base font-semibold pt-3">
        <a
          href="#"
          className="flex items-center bg-active_nav_link text-white py-4 pl-6 nav-item"
        >
          <i className="fas fa-tachometer-alt mr-3"></i>
          Doctor's Dashboard
        </a>
        <Link to="/d/reports">
          <button className="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item">
           <i className="fas fa-table mr-3"></i>Reports
          </button>
        </Link>
        <Link to="/d/Patients">
          <button className="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item">
           <i className="fas fa-table mr-3"></i>Patient List
          </button>
        </Link>
        <a
          href="forms.html"
          className="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item"
        >
          <i className="fas fa-align-left mr-3"></i>
          Account Settings
        </a>
        {/* <a href="tabs.html" className="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item">
          <i className="fas fa-tablet-alt mr-3"></i>
          Tabbed Content
        </a>
        <a href="calendar.html" className="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item">
          <i className="fas fa-calendar mr-3"></i>
          Calendar
        </a> */}
      </nav>
      {/* <a href="#" className="absolute w-full upgrade-btn bottom-0 active-nav-link text-white flex items-center justify-center py-4">
        <i className="fas fa-arrow-circle-up mr-3"></i>
        Upgrade to Pro!
      </a> */}
    </aside>
  );
};

export default Main;
