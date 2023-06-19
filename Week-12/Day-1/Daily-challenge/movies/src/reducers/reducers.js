import { combineReducers } from "redux"

const initState = {
    movies: [
        {id: 1, title: 'Spider-Man: Homecoming', releaseDate: '05-07-2017', rating: 7.4,},
        {id: 2, title: 'Aquaman', releaseDate: '12-07-2018', rating: 7,},
        {id: 3, title: 'Black Panther', releaseDate: '02-13-2018', rating: 7.4,},
        {id: 4, title: 'Avengers: Infinity War', releaseDate: '04-25-2018', rating: 8.3,},
        {id: 5, title: 'Guardians of the Galaxy', releaseDate: '07-30-2014', rating: 7.9,},
    ],
    movie: {
        
    }
}

const moviesReducer = (state = initState, action = {}) => {
    return {...state}
}

const initStateSelect = {
    
}

const selectMovieReducer = (state = initStateSelect,action = {}) => {
    switch(action.type){
        case 'MOVIE_SELECTED':
            console.log(action.payload)
            return {...state, movie:action.payload}
        default:
            return {...state} 
    }
}

const rootReducer = combineReducers(
    {
        moviesReducer,
        selectMovieReducer
    }
)
export default rootReducer
