
import { useState, useEffect, useRef } from "react";
import axios from 'axios';
import {Upload } from 'lucide-react';
import {Link, Routes, Route} from "react-router-dom"

function SendAV() {
    const url = "http://127.0.0.1:5000" //change this to the localhost url
    const [image, setImage] = useState({imageFile: null, imageURL: null})
    const [isUploaded, setIsUploaded] = useState(false)
  
    function handleUpload(e) {
      setImage(() => {
        return {
          imageFile: e.target.files[0],
          imageURL: URL.createObjectURL(e.target.files[0])
        }
      })
    }
    const imageRef = useRef(null);
  
    const handleSkipToTimestamp = () => {
      if (imageRef.current) {
        // Set the desired timestamp (10 seconds in this case)
        imageRef.current.currentTime = startTime;
      }
    };
  
    const [startTime, setStartTime] = useState(0);
  
    useEffect(() => {
      // Adjust the start time as necessary
      setStartTime(10); // Start image at 30 seconds
    }, []);
  
    const handleSubmit = async () => {
      if (image.imageFile !== null) {
        const data = await axios.get(url + '/clear')
        if (data.data.number > 0) {
          const response = await axios.post(url + '/clear')
        }
        const formData = new FormData()
        formData.append(
          'uploaded_file',
          image.imageFile,
          image.imageFile.name
        )
  
        const response = await axios.post(url + '/convert', formData, {
          onUploadProgress: progressEvent => {
            let progress = Math.round(progressEvent.loaded * 100 / progressEvent.total)
            if (progress === 100) {
              setIsUploaded(true)
            }
            console.log(progress + '%')
          }
        })//get upload progress
        console.log(await response)
      }
    }
  
    function isSubmitted() {
      return (
        <div>
          <label htmlFor="submit"
            className="rounded-[25px] w-[70px] text-sm h-[20px] md:h-[60px] md:text-xl bg-textColor text-[#041C44] font-semibold hover:bg-[#949494] flex items-center justify-center cursor-pointer"
          ><Upload size={32} strokeWidth={2} /></label>
          <input type="submit" id="submit" name="submit" className='w-0' onClick={handleSubmit} />
        </div>
      )
    }
  
    return (
      <div className="flex flex-col gap-10">
        <div className="mt-20 bg-[#041C44] flex flex-col items-center max-w-[70vw] rounded-xl pb-10 ">
          <p className="text-center text-2xl mt-10 max-w-[85%]">Wanna find something in your footage? You should image: </p>
  
          <label htmlFor="image"
            className="mt-16 rounded-sm w-[80px] text-sm h-[50px] md:w-[80%] md:h-[60px] md:text-xl bg-secondary text-textColor font-semibold hover:bg-[#1abc9c] flex items-center justify-center cursor-pointer"
          >Select image file</label>
          <input type="file" id="image" name="image" accept="image/*" className='w-0' onChange={handleUpload} required />
  
          {isSubmitted()}
          <div className="flex flex-col justify-center items-center">
          {isUploaded && <image ref={imageRef} controls>
            <source key={image.imageFile.name} src={image.imageURL} type="image/mp4" className="w-[80%] h-auto" />
            Your browser does not support the image tag.
          </image>}
          {isUploaded &&  <Link to='/log'>
      <div className="mt-8 rounded-xl w-[80px] text-md h-[60px] md:w-[30vw] md:text-xl bg-secondary text-textColor font-semibold hover:bg-[#1abc9c] flex items-center justify-center cursor-pointer"
    >View Log</div>
    </Link>}
  
        </div>
        </div>
      </div>
    );
}
export default SendAV;