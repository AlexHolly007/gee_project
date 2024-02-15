import React from 'react'
import '../css/locationGetter.css'

function LocationGetter() {
    return (
        <>
            <div className="location--container">
                <form className="user--input">
                    <label htmlFor="longitude">Longitude: </label>
                    <input type="text" id="longitude" name="longitude"></input>
                    <label htmlFor="latitude">Latitude: </label>
                    <input type="text" id="latitude" name="latitude"></input>
                </form>
            </div>
            <h1>This is where the location will be printed out after user enters</h1>
        </>
    )
}

export default LocationGetter;