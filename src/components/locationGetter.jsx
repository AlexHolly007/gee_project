// import React from 'react'
// import '../css/locationGetter.css'

// function LocationGetter() {
//     return (
//         <>
//             <div className="location--container">
//                 <form className="user--input">
//                     <label htmlFor="longitude">Longitude: </label>
//                     <input type="text" id="longitude" name="longitude"></input>
//                     <label htmlFor="latitude">Latitude: </label>
//                     <input type="text" id="latitude" name="latitude"></input>
//                     <label htmlFor="miles">Miles: </label>
//                     <input type="text" id="miles" name="miles"></input>
//                     <button type="submit">Submit</button>
//                 </form>
//             </div>
//             <h1>This is where the location will be printed out after user enters</h1>
//         </>
//     )
// }

// export default LocationGetter;

import React, { useState } from 'react';
import '../css/locationGetter.css';

function LocationGetter() {
    const [longitude, setLongitude] = useState('');
    const [latitude, setLatitude] = useState('');
    const [miles, setMiles] = useState('');
    const [locationResult, setLocationResult] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await fetch(`http://127.0.0.1:60061/getTimelapse?lon=${longitude}&lat=${latitude}&miles=${miles}`, {
                method: 'GET',
                mode: 'cors',
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            const data = await response.json();
            console.log(data.result[0])
            setLocationResult(data.result); // Assuming API sends back a result
        } catch (error) {
            console.error('Error:', error);
            setLocationResult('Error occurred while fetching data');
        }
    };

    const handleSubmit1 = async (event) => {
        fetch('http://127.0.0.1:60061/getTimelapse?lon=-105&lat=40&miles=10', {
            method: 'GET',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
    }

    return (
        <>
            <div className="location--container">
                <form className="user--input" onSubmit={handleSubmit}>
                    <label htmlFor="longitude">Longitude: </label>
                    <input type="text" id="longitude" name="longitude" value={longitude} onChange={(e) => setLongitude(e.target.value)}></input>
                    <label htmlFor="latitude">Latitude: </label>
                    <input type="text" id="latitude" name="latitude" value={latitude} onChange={(e) => setLatitude(e.target.value)}></input>
                    <label htmlFor="miles">Miles: </label>
                    <input type="text" id="miles" name="miles" value={miles} onChange={(e) => setMiles(e.target.value)}></input>
                    <button type="submit" onClick={handleSubmit}>Submit</button>
                </form>
            </div>
            <h1>{locationResult}</h1>
        </>
    );
}

export default LocationGetter;
