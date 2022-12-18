import React from 'react'
import './tooltip.css'

const Tooltip = ({description, more}) => {
    return (
        <div className="top">
            <h3>{description}</h3>
            <p>{more}</p>
        </div>
    )
}

export default Tooltip