import React, { useState } from 'react'
import Navbar from '../components/landing/navbar'
import LandingPic from '../components/landing/landingPic'
import MainContent from '../components/landing/mainContent'

function Landing() {

    const [isHeaderInterSecting, setIsHeaderIntersecting] = useState(false)

    return (
        <>
            <Navbar />
            <LandingPic />
            <MainContent />
        </>
    )
}

export default Landing