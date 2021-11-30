import { Animal, AnimalPage } from '../datatypes/animal'
import { createAsyncThunk, createSlice } from '@reduxjs/toolkit'
import { useSelector } from 'react-redux'
import {current} from 'immer'

import axios from 'axios';

const initialState = new AnimalPage();

export const fetchAnimalPage = createAsyncThunk('animalPage/fetchAnimalPage',
  async ()=>{
    const response = await axios.get('/animal/')
    console.log(response);
    console.log(response.data)
    return response.data;
  }
) 

export const insertAnimal = createAsyncThunk('animalPage/insertAnimal',
  async (animal)=>{
    const response = await axios.post('/animal/', animal)

    console.log(response);
    console.log(response.data)
    return response.data;
  }
) 

export const deleteAnimal =  createAsyncThunk('animalPage/deleteAnimal',
  async (id, {getState})=>{
    const response = await axios.delete(`/animal/${id}`)
    return id; 
  }
)

export const animalPageSlice = createSlice({
  name: 'animalPage',
  initialState: {}, 
  reducers:{
    dele(state, action){
     state.content = state.content.filter(({id}) => id != "618b05ea00db73e1235e96eb")
     return state;
    },
  },
  extraReducers: {
    [fetchAnimalPage.fulfilled]: (state, action) => {return action.payload},
    [insertAnimal.fulfilled]: (state, action) => {return action.payload},
    [deleteAnimal.fulfilled]: (state, action) => {
      const idPayload = action.payload;
      state.content = state.content.filter(({id}) => id != idPayload)
      return state;
    },
    [deleteAnimal.rejected] : (state, action) => {
      state.msg = 'rejected TESTE'
      alert('rejected')
    }
  },
}); 

export const { dele } = animalPageSlice.actions;

export default animalPageSlice.reducer;
