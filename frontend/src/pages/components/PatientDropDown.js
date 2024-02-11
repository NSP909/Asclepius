import React, { useState, useEffect } from 'react';

const PatientDropDown = ({patients, handlePatientChoice}) => {
    const [isOpen, setIsOpen] = useState(false);
    const [name, setName] = useState("Select an option");

    const toggleDropdown = () => {
      setIsOpen(!isOpen);
    };

  return (
    <div className="relative inline-block text-left mt-5 rounded-sm h-[50px] md:w-[120px] md:h-[60px] md:text-xl">
      <div>
        <button type="button" className="inline-flex justify-center w-full rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
        onClick={toggleDropdown}>
          {name}
          <svg className="-mr-1 ml-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
            <path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" />
          </svg>
        </button>
      </div>
      {isOpen && ( // Render dropdown menu if isOpen is true
        <div className="origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5">
          <div className="py-1" role="menu" aria-orientation="vertical" aria-labelledby="options-menu">
            {patients.map((patient, index) => (
              <button
                key={index}
                className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900 w-full text-left"
                role="menuitem"
                onClick={(e) => {
                    handlePatientChoice(patient.username);
                    setName(patient.fullname)
                    toggleDropdown();
                    console.log('Selected:', patient.fullname)}} // Handle selection
              >
                {patient.fullname}
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default PatientDropDown;
