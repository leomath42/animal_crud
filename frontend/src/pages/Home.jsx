import React from 'react'
import { Link } from 'react-router-dom'
import Table from  '../components/Table'


const Home = () => {
    return (
        <div className="container">
            <div className="row mt-5">
                <div className="col">
                <Link to="/new-animal" className="btn-primary btn">
                    Novo Animal
                </Link>
                </div>
            </div>
            <div className="row mt-4">
                <Table className="col-4"></Table>
            </div>
        </div>
    )
}

export default Home