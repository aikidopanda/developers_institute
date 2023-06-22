const initState = {
    age: 20
}

export const reducer = (state = initState, action = {}) => {
    switch(action.type){
        case 'INCREASE':
            return{...state, age: state.age+1}
        case 'DECREASE':
            return{...state, age: state.age-1}
        default:
            return {...state}
    }
}