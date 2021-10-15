import React from 'react'
import { Link } from 'react-router-dom'
import { useForm } from "react-hook-form"
import axios from 'axios'
import { useHistory } from "react-router-dom";
import { useEffect, useState } from 'react'
import { Animal } from '../datatypes/animal';
import {formatLocalDate} from '../utils/format';
import { ErrorMessage } from '@hookform/error-message';

const AnimalForm = ({ className, reloadFormPage, setReloadFormPage }) => {
    
    const { register, handleSubmit, formState: { errors }, setValue, reset} = useForm({ mode: 'onBlur' });

    const history = useHistory();
    const animal = reloadFormPage;

    const clearFields = () => {
        setReloadFormPage(new Animal())
    }
    const toHome = () => {
        clearFields();
        history.push("/");
    }

    useEffect(() => {
        // loadFields(reloadFormPage)
        setValue('id', reloadFormPage.id, { shouldDirty: true })
        setValue('nome', reloadFormPage.nome, { shouldDirty: true })
        setValue('tipo', reloadFormPage.tipo, { shouldDirty: true })
        setValue('peso', reloadFormPage.peso !== 0  ?  reloadFormPage.peso : '', { shouldDirty: true })
        var value = reloadFormPage.data_nascimento !== "" ?  formatLocalDate(reloadFormPage.data_nascimento,'dd/MM/yyyy'): ''
        setValue('data_nascimento', value, { shouldDirty: true })
    }, [reloadFormPage])

    const onSubmit = (data) => {
        let id = data["id"];
        delete data["id"]
        
        if (id !== 0) {
            axios.put(`/animal/${id}`, data)
                .then(response => {
                    console.log(response);
                    // history.push("/");
                })
                .catch(error => {
                    console.log(error);
                })
                .finally(() => {
                    history.push("/");
                })
        }
        else {
            axios.post('/animal/', data)
                .then(response => {
                    console.log(response);
                    // history.push("/");
                })
                .catch(error => {
                    console.log(error);
                }).finally(() => {
                    history.push("/");
                })
        }
    }

    return (
        <div className={className}>
            <form onSubmit={handleSubmit(onSubmit)} className="container w-50" >
                <ErrorMessage errors={errors} name="singleErrorInput" />
                <div className="jumbotron p-5 bg-dark">
                    <div className="row justify-content-md-center">
                        <div className="col-12 offset-6">
                            <div className="invisible">
                                <input id="id" {...register("id")} type="text" />
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
                                    <select id="tipo" {...register("tipo", { required: true })} className="form-select" aria-label="Tipo">
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
                                    <input  {...register("peso", { required: true })} type="text" id="peso" className="form-control" aria-describedby="Peso" />
                                </div>
                            </div>

                            <div className="form-group row g-3 align-items-center">
                                <div className="col-sm-2 col-form-label">
                                    <label for="data_nascimento" className="col-form-label">Data de Nascimento</label>
                                </div>
                                <div className="col-auto">
                                    <input placeholder="ex: dd/mm/yyyy" {...register("data_nascimento", { required: true , pattern:'/^\d{2}\/\d{2}\/\d{4}$/'})} type="text" id="data_nascimento" className="form-control" aria-describedby="Data" />
                                </div>
                            </div>
                            
                            <div className="form-group row g-3 align-items-center">
                                <div className="col-sm-2 col-form-label">
                                    {/* <Link to="/" className="btn-danger btn form-control">Cancelar</Link> */}
                                    <input type="button" className="btn-danger btn form-control" value="Cancelar" onClick={toHome} />
                                </div>
                                <div className="col-sm-2">
                                    <input type="submit" className="btn-primary btn form-control" value="Salvar"/>
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