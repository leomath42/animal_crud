import React from 'react'
import {BrowserRouter, Route, Switch} from 'react-router-dom'
import Home from './pages/Home'
import AnimalPage from './pages/AnimalPage'
import { useEffect, useState } from 'react'


const Routes = () => {
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/" exact>
                    <Home/>
                </Route>
                <Route path="/new-animal" exact>
                    <AnimalPage/>
                </Route>
            </Switch>
        </BrowserRouter>

        
    )
}
export default Routes