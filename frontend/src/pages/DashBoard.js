import Header from './components/Header';
import { useState, useEffect } from 'react';
import axios from 'axios';
/*[{
        "user_id": patient.user_id, 
        "username": patient.username,
        "fullname": patient.fullname,
        "date_of_birth": patient.date_of_birth,
        "user_height": patient.user_height,
        "user_weight": patient.user_weight,
        "race": patient.race,
        "ethnicity": patient.ethnicity,
        "sex": patient.sex,
        "gender": patient.gender
    } for patient in patients] */

const PatientList = () => {
    const [patients, setPatients] = useState([]);

    useEffect(()=>{
        axios.get('your-api-endpoint-url') //add in the actual endpoint
        .then(response => {
          console.log('Received successfully:', response.data);
          setPatients(response.data);
        })
        .catch(error => {
          console.error('Error in api call:', error);
        });
    },[])

    const genTables=()=>{
        return patients.map((patient)=>{
            return (
                <tr>
                    <td>{patient.user_id}</td>
                    <td>{patient.username}</td>
                    <td>{patient.fullname}</td>
                    <td>{patient.date_of_birth}</td>
                    <td>{patient.sex}</td>
                    <td>{patient.ethnicity}</td>
                </tr>
            )
        })
    }
    return (
        <div className="flex flex-col w-full h-screen overflow-y-hidden items-center">
            <Header/>

        </div>
    );
}

export default PatientList;
