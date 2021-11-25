import React from 'react'
import { Link } from 'react-router-dom'
import Table from '../components/Table'
import { useEffect, useState } from 'react'
import { Animal, AnimalPage } from '../datatypes/animal'
import axios from 'axios'


const Home = () => {
    const [reloadPage, setReloadPage] = useState(false)

    const [page, setPage] = useState(new AnimalPage())

    useEffect(() => {
        axios.get('/animal/').then((response) => {
            setPage(response.data);
        }).catch(error => {
            console.log(error);
        })
    }, [reloadPage])

    function changePage() {
        setReloadPage(!reloadPage);
    }

    return (
        <div className="container">
            <div className="row mt-5">
                <div className="col">
                <Link to="/new-animal" className="btn-primary btn">Novo Animal</Link>
                </div>
            </div>
            <div className="row mt-4">
                <Table className='col-4' page={page} changePage={changePage}></Table>
            </div>
        </div>
    )
}

export default Home
