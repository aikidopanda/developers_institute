const initState = {
    count: 0
}

export const reducer = (state = initState, action = {}) => {
    switch(action.type){
        case 'INCREASE':
            return{...state, count: state.count+1}
        case 'DECREASE':
            return{...state, count: state.count-1}
        case 'INCREMENTIFODD':
            if (state.count%2 !== 0){
                return{...state, count: state.count+1}
            }
            else{
                return{...state}
            }
        case 'INCREMENTASYNC':
            return{...state, count: state.count+1}
        default:
            return {...state}
    }
}