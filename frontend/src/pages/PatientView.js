import React from 'react';

const Sidebar = () => {
  return (
    <aside className="absolute top-0 left-0 pt-4 bg-sidebar h-screen w-64 hidden sm:block shadow-xl">
      <div className="p-3">
        <a href="index.html" className="text-white text-3xl font-semibold uppercase hover:text-gray-300">DuoDoc</a>
        <button className=" mt-10 w-full bg-white cta-btn font-semibold py-2 rounded-br-lg rounded-bl-lg rounded-tr-lg shadow-lg hover:shadow-xl hover:bg-gray-300 flex items-center justify-center">
          <i className="fas fa-plus mr-3"></i> Add Report
        </button>
      </div>
      <nav className="text-white text-base font-semibold pt-3">
        <a href="index.html" className="flex items-center bg-active_nav_link text-white py-4 pl-6 nav-item">
          <i className="fas fa-tachometer-alt mr-3"></i>
          User Dashboard
        </a>
        <a href="blank.html" className="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item">
          <i className="fas fa-sticky-note mr-3"></i>
          My Reports
        </a>
        <a href="tables.html" className="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item">
          <i className="fas fa-table mr-3"></i>
          Predictions
        </a>
        <a href="forms.html" className="flex items-center text-white opacity-75 hover:opacity-100 py-4 pl-6 nav-item">
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
}

export default Sidebar;
