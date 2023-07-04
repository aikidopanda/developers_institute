import robots from '../users.json'

const initState = {
    list: robots, 
}

export const reducer = (state = initState, action = {}) => {
    switch(action.type){
        case 'SEARCH':
            return {
                ...state,
                list: robots.filter((robot) => robot.name.toLowerCase().includes(action.inputsearch.toLowerCase())),
            }
        default:
            return {...state}
    }
}