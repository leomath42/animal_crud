import React from 'react'
import axios from 'axios'

const Button = (props) => {
    // const click = () => {
    //     axios.get('/animal/').then((response) => {
    //         setPage(response.data);
    //         actionEvent();
    //     })
    // }
    return (
        <button className={props.className} onClick={props.onClick}>
            {props.children}
        </button>
    )
}

export default Button