import React from 'react'
import './navbar.css'
import { Link } from "react-router-dom";

const Navbar = () => {
    return (
        <div className='navs'>
            <ul className='navbar'>
                <li>
                    <Link to="/notas">Notas</Link>
                </li>
            </ul>
            <ul className='navbar'>
                <li>
                    <Link to="/">Inicio</Link>
                </li>
                <li>
                    <Link to="/registro">Registro</Link>
                </li>
            </ul>
        </div>
    )
}

export default Navbar