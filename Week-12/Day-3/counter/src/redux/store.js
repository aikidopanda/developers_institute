import {createStore, applyMiddleware} from 'redux'
import thunk from 'redux-thunk'
import { reducer } from './reducer'

const asyncCount = (store) => (next) => (action) => {
    if (action.type === 'INCREMENTASYNC') {
        setTimeout(() => {
            next(action)
        }, 2000)
    } else {
        next(action)
    }
}

const store = createStore(reducer, applyMiddleware(asyncCount, thunk))

export default store