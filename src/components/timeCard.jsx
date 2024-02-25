import React, { useState, useEffect } from 'react'
import '../css/timeCard.css'

export default function timeCard() {

    const [imageIndex, setImageIndex] = useState(0)
    const images = ['output0.png', 'output1.png', 'output2.png', 'output3.png', 'output4.png', 'output5.png',
    'output6.png','output7.png','output8.png','output9.png','output10.png','output11.png','output12.png','output13.png','output14.png','output15.png',
    'output16.png','output17.png','output18.png','output19.png','output20.png','output21.png','output22.png','output23.png','output24.png','output25.png',
    'output26.png','output27.png','output28.png','output29.png','output30.png','output31.png','output32.png','output33.png','output34.png','output35.png','output36.png',
    'output37.png','output38.png']

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