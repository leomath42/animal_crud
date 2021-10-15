import React from 'react'
import {BrowserRouter, Route, Switch} from 'react-router-dom'
import Home from './pages/Home'
import AnimalForm from './pages/AnimalForm'

const Routes = () => {
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/" exact>
                    <Home/>
                </Route>
                <Route path="/new-animal" exact>
                    <AnimalForm/>
                </Route>
            </Switch>
        </BrowserRouter>

        
    )
}
export default Routes