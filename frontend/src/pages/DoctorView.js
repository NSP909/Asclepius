import { SquareUser } from 'lucide-react';
import { Link, Routes, Route } from "react-router-dom";
import React from "react";
import AddReport from "./AddReport";
import DashBoard from "./DashBoard";

import PatientsList from "./PatientList";
import SearchPredict from "./SearchPredict";
import SearchBarResults from "./SearchPredict";

const Main = () => {
  return (
    <div className="flex w-full h-screen overflow-y-hidden">
      <Sidebar />
      
      <Routes>
        <Route path="/add" element={<AddReport />} />
        <Route path="/" element={<DashBoard />} />
        <Route path="/Patients" element={<PatientsList />} />
        <Route path="/Search" element={<SearchBarResults />} />
      </Routes>
    </div>
  );
};

const Sidebar = () => {
  return (
    <aside className="pt-4 bg-sidebar h-screen min-w-64 hidden sm:block shadow-xl">
      <div className="p-3">
        <a
          href="#"
          className="text-white text-3xl font-semibold hover:text-gray-300"
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
       
        <Link to="/d/Patients">
          <button  className="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item">
            <i className="fas fa-users mr-3"></i> Patient List
          </button>
        </Link>
        <Link to="/d/Search">
          <button  className="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item">
            <i className="fas fa-plus mr-3"></i> Search
          </button>
        </Link>
        <a
          href="forms.html"
          className="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item"
        >
          <i className="fas fa-align-left mr-3"></i>
           Settings
        </a>
      </nav>
    </aside>
  );
};

export default Main;
