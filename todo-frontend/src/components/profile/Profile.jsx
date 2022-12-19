import React from 'react'
import ButtonCircle from '../note/circle/ButtonCircle'

const Profile = () => {
  return (
    <div className='register'>
        <ButtonCircle/>
        <ul>
            <li>Username:</li>
            <li className='password'>Password:</li>
        </ul>
    </div>
  )
}

export default Profile