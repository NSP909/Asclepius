import axios from "axios";

const FullReport = async (userId) => {
  try {
    // Make Axios GET request with user ID as a parameter
    const response = await axios.post('http://104.248.110.113:5000/getentirehistory', { user_id: userId });
    console.log(response.data);
    return response.data;
    // Handle response data or other actions here
  } catch (error) {
    console.error('Error fetching full report:', error);
    throw error; // Rethrow the error so that the caller can handle it
  }
};

export default FullReport;