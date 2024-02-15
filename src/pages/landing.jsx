import React from 'react'
import LandingPic from '../components/landingPic'
import MainContent from '../components/mainContent'
import LocationGetter from '../components/locationGetter'
import TimeCard from '../components/timeCard'

function Landing() {

    return (
        <>
            <LandingPic />
            <MainContent />
            <LocationGetter />
            <TimeCard />
        </>
    )
}

export default Landing