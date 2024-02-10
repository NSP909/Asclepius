import { useState } from 'react';
import React from 'react';


const Header = () => {
    const [isOpen, setIsOpen] = useState(false);
  
    return (
      <header className="w-full items-center bg-gray-100 border-b border-b-gray-700 py-2 px-6 hidden sm:flex">
        <div className="w-1/2"></div>
        <div className="relative w-1/2 flex justify-end">
          <button onClick={() => setIsOpen(!isOpen)} className="relative z-10 w-12 h-12 rounded-full overflow-hidden border-4 border-gray-400 hover:border-gray-300 focus:border-gray-300 focus:outline-none">
            <img src="https://source.unsplash.com/uJ8LNVCBjFQ/400x400" alt="Profile" /> {/* This is a placeholder image */}
          </button>
          {isOpen && <button onClick={() => setIsOpen(false)} className="h-full w-full fixed inset-0 cursor-default"></button>}
          {isOpen && 
            <div className="absolute w-32 bg-white rounded-lg shadow-lg py-2 mt-16">
              <a href="#" className="block px-4 py-2 account-link hover:text-white">Account</a>
              <a href="#" className="block px-4 py-2 account-link hover:text-white">Support</a>
              <a href="#" className="block px-4 py-2 account-link hover:text-white">Sign Out</a>
            </div>
          }
        </div>
      </header>
    );
  }

export default Header;