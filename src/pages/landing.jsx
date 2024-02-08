import React from 'react'
import Navbar from '../components/landing/navbar'
import LandingPic from '../components/landing/landingPic'
import MainContent from '../components/landing/mainContent'

function Landing() {
    return (
        <>
            <Navbar />
            <LandingPic />
            <MainContent />
        </>
    )
}

export default Landing