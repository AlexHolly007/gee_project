// navbar.js

import React from 'react'
import '../css/navbar.css'

function Navbar() {
    return (
        <>
            <nav className="navbar">
                <a className="navbar--links" href="index.html">Home</a>
                <a className="navbar--links" href="about.html">About Us</a>
                <a className="navbar--links" href="main.html">Our Project</a>
                <a className="navbar--links" href="contact.html">Contact Us</a>
            </nav>
        </>
    )
}

export default Navbar