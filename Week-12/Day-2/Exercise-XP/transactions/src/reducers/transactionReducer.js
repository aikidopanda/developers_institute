import initState from "../data"

export const transactionReducer = (state = initState, action = {}) => {
    switch(action.type){
        case 'INSERT':
            console.log(action.payload)
            return {...state, data: [...state.data,action.payload]}
        case 'UPDATE':
            let list = [...state.data];
            list[state.currentIndex] = action.payload;
            return {
                ...state,
                data: list
            };
        case 'DELETE':
            return {
                ...state,
                data: state.data.filter(transaction => transaction.accountNumber !== action.payload.accountNumber)
            };
        case 'UPDATE-INDEX':
            return{...state, currentIndex: action.payload}
        default:
            return {...state}
    }
}