import React from 'react'
import AnimalForm from '../components/AnimalForm'
import { useEffect, useState } from 'react'


const AnimalPage = (animalPage) => {
    return (
        <AnimalForm className="mt-5" reloadFormPage={animalPage.reloadFormPage} setReloadFormPage={animalPage.setReloadFormPage} />
    )
}

export default AnimalPage