import React from 'react'

const Table = () => {
    // Mock data Table
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
                    <tr>
                        <td>25/10/2020</td>
                        <td>Zeus</td>
                        <td>Cachorro</td>
                        <td>10 Kg</td>
                        <td>Alterar</td>
                        <td>Excluir</td>
                    </tr>
                    <tr>
                        <td>25/10/2020</td>
                        <td>Zeus</td>
                        <td>Cachorro</td>
                        <td>10 Kg</td>
                        <td>Alterar</td>
                        <td>Excluir</td>
                    </tr>
                    <tr>
                        <td>25/10/2020</td>
                        <td>Zeus</td>
                        <td>Cachorro</td>
                        <td>10 Kg</td>
                        <td>Alterar</td>
                        <td>Excluir</td>
                    </tr>
                </tbody>
            </table>
        </div>
    )
}

export default Table