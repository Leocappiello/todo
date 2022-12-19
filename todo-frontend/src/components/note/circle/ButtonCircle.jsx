import React from 'react'
import './circle.css'

const ButtonCircle = ({name, color}) => {
  return (
    <div style={{backgroundColor:color}} className='circle'>{name}</div>
  )
}

export default ButtonCircle