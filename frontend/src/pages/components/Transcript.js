import { useState, useEffect } from "react";
import axios from "axios";

const Transcript = ({transdata, patient}) => {
    const onSubmit = async () => {
        try {
            const response = await axios.post('http://104.248.110.113:5000/save', {
              data: {...transdata, username: patient},
            });
            console.log('Response:', response.data);
            return response.data;
          } catch (error) {
            console.error('Error:', error);
          }
    }

    return (
      <div className="flex flex-col">
        <div className=" bg-gray-200 h-[50vh] max-h-[50vh] w-[60vw] overflow-y-auto border-dashed border-2 border-gray-300 p-4">
            <pre className="text-left pt-4">{transdata}</pre> 
        </div>
        <div className="flex justify-center">
        <label
          htmlFor="text"
          className="mt-5 rounded-md w-[80px] text-sm h-[50px] md:w-[15vw] md:h-[60px] md:text-xl bg-headerColor text-textColor font-semibold hover:bg-sidebar flex items-center justify-center cursor-pointer shadow-md"
        >
          Save
        </label>
        <input
          type="submit"
          id="text"
          name="text"
          accept="text/*"
          className="w-0"
          onSubmit={onSubmit}
          required
        />
      </div>
      </div>
    );
  };
  

export default Transcript;