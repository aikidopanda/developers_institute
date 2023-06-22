import {createStore, applyMiddleware} from 'redux'
import thunk from 'redux-thunk'
import { reducer } from './reducer'

const logger = (store) => (next) => (action) => {
    console.log('Caught in the middleware:', store.getState().age)
    return next(action)
}

const store = createStore(reducer, applyMiddleware(logger, thunk))

export default store