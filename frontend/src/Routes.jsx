import React from 'react'
import { BrowserRouter, Route, Switch, useHistory} from 'react-router-dom'
import Home from './pages/Home'
import AnimalPage from './pages/AnimalPage'
import { Animal } from './datatypes/animal'
import { useEffect, useState } from 'react'

const Routes = () => {

    return (
          <BrowserRouter>
              <Switch>
                  <Route path="/" exact>
                      <Home  />
                  </Route>
                  <Route path={["/new-animal", "/new-animal/:id"]} exact>
                      <AnimalPage  />
                  </Route>
              </Switch>
          </BrowserRouter>
    )
}
export default Routes
