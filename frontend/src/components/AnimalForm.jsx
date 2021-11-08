import React from 'react';
import { Link } from 'react-router-dom';
import { useForm } from "react-hook-form";
import axios from 'axios';
import { useHistory, useParams } from "react-router-dom";
import { useEffect, useState } from 'react';
import { Animal } from '../datatypes/animal';
import {formatLocalDate, formatDateToDatePicker } from '../utils/format';

const AnimalForm = ({className}) => {

  const history = useHistory();
  const { id } = useParams();
  const [animalForm, setAnimalForm] = useState({});

  const toHome = () => {
    history.push("/");
  }

  const handleInputChange = (e) => {
    setAnimalForm({...animalForm, [e.target.name]: e.target.value});
  }

  const handleSubmit = async (e) => {
    e.preventDefault();

    animalForm.data_nascimento = formatLocalDate(animalForm.data_nascimento, "dd/MM/yyyy"); 

    try {
      let response = await axios.post('/animal/', animalForm);
      console.log(response);
      history.push("/");
    } catch (exception) {
      console.error(exception)
    }

  };

  // seta o formulário em caso de update
  useEffect(
    async () => {
      if(id !== undefined){
        let response = await axios.get(`/animal/${id}`);
        var animal = new Animal({...response.data});
        animal.data_nascimento = formatDateToDatePicker(animal.data_nascimento); 
        setAnimalForm(animal);
        document.querySelector('input[type="date"]').value = animal.data_nascimento;
      }
    }, []
  )

  return (
      <div className={className}>
          <form className="container w-50" onSubmit={handleSubmit} >
              <div className="jumbotron p-5 bg-dark">
                  <div className="row justify-content-md-center">
                      <div className="col-12 offset-6">
                          <div className="invisible">
                              <input id="id" type="text" />
                          </div>
                          <div className="form-group row g-3 align-items-center">
                              <label for="Nome" className="col-sm-2 mt-4 col-form-label">Nome</label>
                              <div className="col-auto">
                                  <input type="text" id="nome" name="nome" classname="form-control" aria-describedby="nome" onChange={handleInputChange} value={animalForm.nome}/>
                              </div>
                          </div>

                          <div className="form-group row g-3 align-items-center">
                              <div className="col-sm-2 col-form-label">
                                  <label for="Tipo" className="col-sm-2  mt-4 col-form-label">Tipo</label>
                              </div>
                              <div className="col-auto">
                                  <select id="tipo" className="form-select" aria-label="Tipo" tipo="tipo" name="tipo" onChange={handleInputChange} value={animalForm.tipo}>
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
                                  <input type="text" id="peso" className="form-control" aria-describedby="Peso" name="peso" onChange={handleInputChange} value={animalForm.peso} />
                              </div>
                          </div>

                          <div className="form-group row g-3 align-items-center">
                              <div className="col-sm-2 col-form-label">
                                  <label for="data_nascimento" className="col-form-label">Data de Nascimento</label>
                              </div>
                              <div className="col-auto">
                                  <input type="date" id="data_nascimento" className="form-control" aria-describedby="Data" name="data_nascimento" onChange={handleInputChange} value={animalForm.date}/>
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
