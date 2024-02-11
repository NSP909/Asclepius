import React from "react";
import axios from "axios"; // Don't forget to import axios

const FullReport = async (userId) => {
  try {
    // Make Axios GET request with user ID as a parameter
    const response = await axios.post('http://104.248.110.113:5000/getentirehistory', 
    { user_id: userId} 
      );
    console.log(response.data);

    // Handle response data or other actions here
  } catch (error) {
    console.error('Error fetching full report:', error);
  }
};

export default FullReport;

