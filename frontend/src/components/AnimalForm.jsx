import React from 'react'
import { Link } from 'react-router-dom'
import { useForm } from "react-hook-form"
import axios from 'axios'
import { useHistory } from "react-router-dom";

const AnimalForm = (param) => {
    const { register, handleSubmit } = useForm();
    const history = useHistory();

    const onSubmit = (data) => {
        console.log(data)
        axios.post('/animal/', data)
          .then( response => {
            console.log(response);
            history.push("/");
          })
          .catch( error => {
            console.log(error);
          });
    }
    return (
        <div className={param.className}>
            <form onSubmit={handleSubmit(onSubmit)} className="container w-50" >
                <div className="jumbotron p-5 bg-dark">
                    <div className="row justify-content-md-center">
                        <div className="col-12 offset-6">
                            <div className="invisible">
                                <input value="" {...register("id")} type="text"/>
                            </div>
                            <div className="form-group row g-3 align-items-center">
                                <label for="Nome" className="col-sm-2 mt-4 col-form-label">Nome</label>
                                <div className="col-auto">
                                    <input {...register("nome", { required: true, maxLength: 20 })} type="text" id="nome" className="form-control" aria-describedby="Nome" />
                                </div>
                            </div>

                            <div className="form-group row g-3 align-items-center">
                                <div className="col-sm-2 col-form-label">
                                    <label for="Tipo" className="col-sm-2  mt-4 col-form-label">Tipo</label>
                                </div>
                                <div className="col-auto">
                                    <select {...register("tipo", { required: true})} className="form-select" aria-label="Tipo">
                                        <option selected></option>
                                        <option value="cachorro">Cachorro</option>
                                        <option value="gato">Gato</option>
                                        <option value="papagaio">Papagaio</option>
                                        <option value="hamster">hamster</option>
                                    </select>
                                </div>
                            </div>

                            <div className="form-group row g-3 align-items-center">
                                <div className="col-sm-2 col-form-label">
                                    <label for="Peso" className="col-form-label">Peso</label>
                                </div>
                                <div className="col-auto">
                                    <input {...register("peso", { required: true})} type="text" id="Peso" className="form-control" aria-describedby="Peso" />
                                </div>
                            </div>

                            <div className="form-group row g-3 align-items-center">
                                <div className="col-sm-2 col-form-label">
                                    <label for="data_nascimento" className="col-form-label">Data de Nascimento</label>
                                </div>
                                <div className="col-auto">
                                    <input {...register("data_nascimento", { required: true})} type="text" id="data_nascimento" className="form-control" aria-describedby="Data" />
                                </div>
                            </div>

                            <div className="form-group row g-3 align-items-center">
                                <div className="col-sm-2 col-form-label">
                                    <Link to="/" className="btn-danger btn form-control">Cancelar</Link>
                                </div>
                                <div className="col-sm-2">
                                    <input type="submit" className="btn-primary btn form-control" value="Salvar" />
                                </div>
                            </div>
                        </div>

                    </div>

                </div>
            </form>
        </div>

    )
}

export default AnimalForm