import React from 'react'
import { Link } from 'react-router-dom'
import Table from '../components/Table'
import { useEffect, useState } from 'react'
import { Animal, AnimalPage } from '../datatypes/animal'
import axios from 'axios'
import {useSelector, useDispatch} from 'react-redux'
import {fetchAnimalPage} from '../slices/AnimalPageSlice'
import {store} from '../store'

//store.dispatch(fetchAnimalPage())

const Home = () => {
  console.count('mounted')

  const dispatch = useDispatch();
  const page2  = useSelector(state => state.animalPage);

  useEffect(() =>{
    if(Object.entries(page2).length == 0){
      dispatch(fetchAnimalPage())
    }
    //dispatch(fetchAnimalPage())
    console.count();
  }, [page2])

  const [page, setPage] = useState(new AnimalPage())

  //useEffect(() =>{
    //setPage(page2)
    //console.count('setPage');
  //}, [page2])

  console.log(page2)
  
  const [reloadPage, setReloadPage] = useState(false)

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
              <Table className='col-4' page={page2} changePage={changePage}></Table>
          </div>
      </div>
  )
}

export default Home
