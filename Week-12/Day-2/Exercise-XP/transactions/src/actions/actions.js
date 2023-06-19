export const insertPayment = (data) => {
    return{
        type: 'INSERT',
        payload: data
    }
}

export const updatePayment = (data) => {
    return{
        type: 'UPDATE',
        payload: data
    }
}

export const deletePayment = (id) => {
    return{
        type: 'DELETE',
        payload: id
    }
}

export const updateIndex = (index) => {
    return{
        type: 'UPDATE-INDEX',
        payload: index
    }
}