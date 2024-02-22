import React from 'react'
import '../css/timeCard.css'

export default function timeCard(props) {

    const { image } = props


    return (
        <>
            <div className='timeContainer'>
                <img className="bigCard" src={image}>
                </img>
            </div>
        </>
    )
}