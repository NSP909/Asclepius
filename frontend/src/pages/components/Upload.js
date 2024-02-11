import { useState, useEffect } from "react";
import axios from "axios";
import Transcript from "./Transcript";
import PatientDropDown from "./PatientDropDown";

//fucntion to upload base64 converted image to the server
function SendAV() {
  const url = "http://127.0.0.1:5000"; //change this to the localhost url
  const [selectedFile, setSelectedFile] = useState(null);
  const [fileName, setFileName] = useState('');
  const [transcriptData, setTranscriptData] = useState('');
  const [patientsData, setPatientsData] = useState([]);
  const [patientChoice, setPatientChoice] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://104.248.110.113:5000/getpatients");
        const data = await response.json();
        setPatientsData(data);
        console.log(data);
      } catch (error) {
        console.error("Error fetching patient data:", error);
      }
    }
    fetchData();
  },[])

  useEffect(() => {
    handleUpload();
  },[selectedFile]);
  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
    console.log(e.target.files[0]);
    setFileName(e.target.files[0].name);
  };

  //to store the patient choice 
  const handlePatientChoice = (e) => {
    setPatientChoice(e.target.value);
  }


  const handleUpload = () => {
    
    if (selectedFile == null) {
      console.error('No file selected');
      return;
    }
    // console.log('this is running')
    const reader = new FileReader();
    reader.readAsDataURL(selectedFile);

    reader.onload = () => {
      const base64Image = reader.result.split(',')[1];
      console.log(base64Image)
      
      axios.post('http://104.248.110.113:5000/transcribe', { imagebase64: base64Image }) //add in the actual endpoint
        .then(response => {
          console.log('Image uploaded successfully:', response.data);
          setTranscriptData(response.data);
        })
        .catch(error => {
          console.error('Error uploading image:', error);
        });
    };

    reader.onerror = () => {
      console.error('Failed to read file');
    };
  };

  return (
    <div className="flex flex-col font-['Nunito Sans']">
      <div className="mt-5 bg-textColor flex flex-col items-center max-w-[70vw] rounded-xl pb-10 ">
        <p className="px-10 text-center text-2xl mt-5 max-w-[100%]">
          Upload clinical records{" "}
        </p>
        <div className="flex justify-center w-[100%]">
          <PatientDropDown patients={patientsData} handlePatientChoice={handlePatientChoice}/>
          <label
          htmlFor="image"
          className="mt-5 rounded-sm w-[80px] text-sm h-[50px] md:w-[50%] md:h-[60px] md:text-xl bg-headerColor text-textColor font-semibold hover:bg-sidebar flex items-center justify-center cursor-pointer shadow-md"
        >
          Select image file
        </label>
        <input
          type="file"
          id="image"
          name="image"
          accept="image/*"
          className="w-0"
          onChange={(e) => {
            handleFileChange(e);
          }}
          required
        />
        </div>
        {fileName && <p>Chosen file: {fileName}</p>}
      </div>
      <Transcript text={transcriptData}/>
    </div>
  );
}





export default SendAV;






// const UploadImage = () => {
//   const [selectedFile, setSelectedFile] = useState(null);

//   const handleFileChange = (e) => {
//     setSelectedFile(e.target.files[0]);
//   };

//   const handleUpload = () => {
//     if (!selectedFile) {
//       console.error('No file selected');
//       return;
//     }

//     const reader = new FileReader();
//     reader.readAsDataURL(selectedFile);

//     reader.onload = () => {
//       const base64Image = reader.result.split(',')[1];
      
//       axios.post('your-api-endpoint-url', { image: base64Image })
//         .then(response => {
//           console.log('Image uploaded successfully:', response.data);
//         })
//         .catch(error => {
//           console.error('Error uploading image:', error);
//         });
//     };

//     reader.onerror = () => {
//       console.error('Failed to read file');
//     };
//   };

//   return (
//     <div>
//       <input type="file" onChange={handleFileChange} />
//       <button onClick={handleUpload}>Upload Image</button>
//     </div>
//   );
// }

// const handleSubmit = async () => {
//   if (image.imageFile !== null) {
//     const data = await axios.get(url + "/clear");
//     if (data.data.number > 0) {
//       const response = await axios.post(url + "/clear");
//     }
//     const formData = new FormData();
//     formData.append("uploaded_file", image.imageFile, image.imageFile.name);

//     const response = await axios.post(url + "/convert", formData, {
//       onUploadProgress: (progressEvent) => {
//         let progress = Math.round(
//           (progressEvent.loaded * 100) / progressEvent.total
//         );
//         if (progress === 100) {
//           setIsUploaded(true);
//         }
//         console.log(progress + "%");
//       },
//     }); //get upload progress
//     console.log(await response);
//   }
// };