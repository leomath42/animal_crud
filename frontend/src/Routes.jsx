import React from 'react'
import { BrowserRouter, Route, Switch, useHistory} from 'react-router-dom'
import Home from './pages/Home'
import AnimalPage from './pages/AnimalPage'
import { Animal } from './datatypes/animal'
import { useEffect, useState } from 'react'

const Routes = () => {
    const [reloadFormPage, setReloadFormPage] = useState(new Animal());

    return (
        <BrowserRouter>
            <Switch>
                <Route path="/" exact>
                    <Home reloadFormPage={reloadFormPage} setReloadFormPage={setReloadFormPage} />
                </Route>
                <Route path="/new-animal" exact>
                    <AnimalPage reloadFormPage={reloadFormPage} setReloadFormPage={setReloadFormPage} />
                </Route>
            </Switch>
        </BrowserRouter>


    )
}
export default Routes