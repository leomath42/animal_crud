import { configureStore } from '@reduxjs/toolkit'
import AnimalPageSlice from './slices/AnimalPageSlice' 

export const store = configureStore({
  reducer: {
    animalPage: AnimalPageSlice,
    msg: {}
  }
})
