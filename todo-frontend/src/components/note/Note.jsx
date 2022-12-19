import React from 'react'
import './note.css'
/* import ButtonCircle from './circle/ButtonCircle' */

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPenToSquare, faCircleXmark, faEye } from '@fortawesome/free-solid-svg-icons'
import Tooltip from './tooltip/Tooltip'



const Note = ({title="Note", description="Description"}) => {
    return (
        <div className='note'>
            <div className="photo">
                <span className="photoSquare" />
            </div>
            <div className="description">
                <h4>{title}</h4>
                <p>{description}</p>
            </div>
            <div className="options">

                <div className="btn btn-primary tooltip">
                    <FontAwesomeIcon className='btn btn-primary tooltip' size="xl" icon={faEye} style={{ color: "#1FA0DE" }} />
                    <Tooltip description="Ver detalles" more="Ver los detalles de la nota"></Tooltip>
                </div>

                <div className="btn btn-primary tooltip">
                    <FontAwesomeIcon size="xl" icon={faPenToSquare} style={{ color: "#DED71F" }} />
                    <Tooltip description="Editar" more="Muestra todos los detalles dentro de la nota"></Tooltip>
                </div>


                <div className="btn btn-primary tooltip">
                    <FontAwesomeIcon size="xl" icon={faCircleXmark} style={{ color: "#DE0922" }} />
                    <Tooltip description="Eliminar" more="Elimina una nota de la lista" ></Tooltip>
                </div>

            </div>
        </div>
    )
}

export default Note