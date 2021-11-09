import { Animal, AnimalPage } from '../datatypes/animal'
import { createAsyncThunk, createSlice } from '@reduxjs/toolkit'

import axios from 'axios';

const initialState = new AnimalPage();

//export async function fetchAnimalPage(dispatch, getState){
  
//}

export const fetchAnimalPage = createAsyncThunk('animalPage/fetchAnimalPage',
  async ()=>{
    const response = await axios.get('/animal/')
    console.log(response);
    console.log(response.data)
    return response.data;
  }
) 

//export default function animalPageReducer(animalPage = initialState, action){
//}
export const animalPageSlice = createSlice({
  name: 'animalPage',
  initialState: {}, 
  reducers:{},
  extraReducers: {
    [fetchAnimalPage.fulfilled]: (state, action) => {return action.payload}
  },
}); 

//export default function animalPageReducer(animalPage = initialState, action){
  //switch (action.type) {
    //case 'getPage':{
      //return action.payload; 
      //break; 
    //}
    //default:
      //return animalPage;
  //}
//}
export default animalPageSlice.reducer;
