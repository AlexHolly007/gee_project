import React, { useState, useEffect } from 'react'
import '../css/timeCard.css'

export default function timeCard() {

    const [imageIndex, setImageIndex] = useState(0)
    const images = ['output0.png', 'output1.png', 'output2.png', 'output3.png', 'output4.png']

    useEffect(() => {
        const interval = setInterval(() => {
            setImageIndex((prevIndex) => (prevIndex + 1) % images.length)
        }, 500)

        return () => clearInterval(interval)
    }, [])

    return (
        <>
            <div className='timeContainer'>
                <img className="bigCard" src={`/Timelapse/${images[imageIndex]}`}>
                </img>
            </div>
        </>
    )
}