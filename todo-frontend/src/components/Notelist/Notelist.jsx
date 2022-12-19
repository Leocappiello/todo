import React from 'react'
import Note from '../note/Note'

const Notelist = ({loading, data}) => {
  return (
    <>
        {loading ? <h2>Loading...</h2> : <Note loading={loading} />}
        {!loading && data.map((elem, index) =>
          <Note key={index} title={elem.name} description={elem.username} loading={loading} />
        )} 
    </>
  )
}

export default Notelist