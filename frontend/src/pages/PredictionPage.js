import { useParams } from 'react-router';
import React, { useState, useEffect } from "react";
import Header from './components/Header';
import Prediction from './Prediction';
import axios from "axios";

const PredictionPage = () => {
    const { id } = useParams();
    const reportId = parseInt(id);
    const [predictionData, setprediction] = new useState(null);
    useEffect(() => {
        const fetchData = async () => { 
          try {
            const response = await Prediction(reportId);
            console.log("prediction response " + response)
            // const parsedData = JSON.parse(response.data);
            setprediction(response.prediction);
          } catch (error) {
            console.error('Error fetching data:', error);
          }
        };
        fetchData();
        console.log("this is the summmmmmary" + Prediction(reportId));

      }, []);
    return (
        <div className="flex flex-col w-full h-screen overflow-y-hidden items-center">
            <Header/>
            <h1 className="mt-5 text-3xl font-bold mb-4 font-karla">Patient id: {id}</h1>
            <div className="mt-20 bg-gray-200 h-[50vh] max-h-[50vh] w-[60vw] overflow-y-auto border-dashed border-2 border-gray-300 p-4">
                <pre className="text-left pt-4 text-wrap">{predictionData}</pre> 
            </div>
        </div>
    );
}

export default PredictionPage;