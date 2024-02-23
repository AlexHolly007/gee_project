import React, { useState, useEffect } from 'react'
import '../css/timeCard.css'

/**
 * function getPictureStyle() {
        fetch('/make_request', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(''),
        })
        .then(response => response.json())
        .then(data => {
            picture_style = data['result'];// Saving the picture style for further use. It is a global variable.
        })
        .catch(error => { //error checking
            responseContainer.innerHTML = error;
            console.error('Error:', error);
        });
    }
    getPictureStyle();
 * 
 */

export default function timeCard() {

    const [images, setImages] = useState([]);
    const [index, setIndex] = useState(0);

    useEffect(() => {
        // Fetch list of image names from backend route
        // try {
        //     const response = await fetch(
        //         `http://127.0.0.1:60061/getTimelapse/?=${}`
        //     )
        // }
    }, []);

    useEffect(() => {
        const interval = setInterval(() => {
            setIndex(i => (i + 1) % images.length);
        }, 100);
        return () => clearInterval(interval);
    }, [images]);

    return (
        <>
            <div className='timeContainer'>
                <img className="bigCard" src={`/images/${images[index]}`}>
                </img>
            </div>
        </>
    )
}