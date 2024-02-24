import React from 'react'
import '../css/mainContent.css'

function MainContent() {
    return (
        <>
            <div className="content--container">
                <p>
                    This project aims to be a way people can see the affects of climate change around them. We feel that too many people are not aware or they just don't care.
                    This is a very simple program that lets you enter a longitude and a latitude of your desired location.
                    After you enter those details you have a field to enter miles, this is how far apart you want timelapse to capture.
                </p>
                <p>
                My friend and I leveraged our front-end and back-end development skills to build a website aimed at tackling land use issues for the Google solutions challenge.
                As the front-end developer, I used React with Vite to rapidly develop the UI components and single page application functionality. Vite streamlined the build 
                process through optimized bundling and efficient hot module replacement. For the back-end, my partner implemented a Flask server to handle our API and data piping,
                allowing flexibility to customize just the endpoints we needed. The powerhouse for data analysis was Google Earth Engine's geospatial capabilities and rich satellite 
                imagery catalogs which enabled streamlined processing at scale. With React facilitating dynamic and reactive UI, Flask enabling customized API creation, and Earth 
                Engine's geospatial muscle, our stack offered a strong foundation. Given our novice experience levels, these choices provided a lightweight yet scalable base for 
                developing a functional prototype website to showcase potential solutions to challenging land problems.
                </p>
        </div>
    </>
    )
}

export default MainContent;