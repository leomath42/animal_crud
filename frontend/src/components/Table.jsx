import axios from 'axios'
import React from 'react'
import { useEffect, useState } from 'react'
import { Animal, AnimalPage } from '../datatypes/animal'
import {formatLocalDate} from '../utils/format'
import Button from './Button'
// import Button from '../components/Button'

const Table = (page, changePage) => {

    // const [reloadPage, setReloadPage] = useState(false)

    // const [page, setPage] = useState(new AnimalPage())

    // // Mock data Table
    // useEffect(() => {
    //     axios.get('/animal/').then((response) => {
    //         setPage(response.data);
    //         console.log(response.data)
    //     })
    // }, [reloadPage])

    // const changePage = () => {
    //     setReloadPage(!changePage)
    // }
    useEffect(() => {
        changePage();
      }, []);

    const clickDelete = (id) => {
        axios.delete(`/animal/${id}`).then((response) => {
            changePage();
        })
    }
    return (
        <div className="table-responsive">
            <table className="table table-striped table-sm table-dark">
                <thead>
                    <tr>
                        <td>Data de Nascimento</td>
                        <td>Nome</td>
                        <td>Tipo</td>
                        <td>Peso</td>
                        <td>Alterar</td>
                        <td>Excluir</td>
                    </tr>
                </thead>
                <tbody>
                    {page.content?.map(item => (
                        <tr key={item.id}>
                            <td>{formatLocalDate(item.data_nascimento, 'dd/MM/yyyy')}</td>
                            <td>{item.nome}</td>
                            <td>{item.tipo}</td>
                            <td>{item.peso}</td>
                            <td>Alterar</td>
                            <td><Button className="btn-danger btn" onClick={()=> {clickDelete(item.id)}}>Excluir</Button></td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default Table