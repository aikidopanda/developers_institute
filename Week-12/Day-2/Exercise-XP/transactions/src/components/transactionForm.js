import React from 'react'
import { connect } from 'react-redux'
import {transactionReducer} from '../reducers/transactionReducer'
import { insertPayment, updatePayment, deletePayment, updateIndex } from '../actions/actions'

//updating function doesn't work, should ask teachers about local storage, probably its the case
//deletion works but I dont think that my method is optimal
//so the task wasnt fully complete, I am just uploading everything I had done by now

class TransactionForm extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            accountNumber: this.state.accountNumber || '',
            fsc: this.state.fsc || '',
            name: this.state.name || '',
            amount: this.state.amount || ''
        }
    }

    handleChange = (event) => {
        event.preventDefault()
        this.setState({[event.target.name]:event.target.value})
    }

    handleSubmit = (event) => {
        event.preventDefault()
        if (this.props.currentIndex == -1){
            this.props.insertPayment(this.state)
        }
        else{
            this.props.updatePayment(this.state)
        }
        this.setState({
            accountNumber: '',
            fsc: '',
            name: '',
            amount: ''
        })
    }

    handleEdit = (index) => {
        let transactionCurrent = this.props.data[index]
        if (transactionCurrent) {
            this.setState({ 
                accountNumber: transactionCurrent.accountNumber, 
                fsc: transactionCurrent.fsc, 
                name: transactionCurrent.name, 
                amount: transactionCurrent.amount
            });
            this.props.updateIndex(index)
        }

    }

    handleDelete = (index) => {
        const transactionCurrent = this.props.data[index];
        if (transactionCurrent) {
          this.props.deletePayment(transactionCurrent);
        }
      };

    render(){
        return(
            <>
                <h1>Enter transaction details</h1>
                <form onSubmit={this.handleSubmit}>
                    Account Number: <input name='accountNumber' value={this.state.accountNumber} onChange={this.handleChange}/>
                    FSC: <input name='fsc' value={this.state.fsc} onChange={this.handleChange}/>
                    Name: <input name='name' value = {this.state.name} onChange={this.handleChange}/>
                    Amount: <input name='amount' value = {this.state.amount} onChange={this.handleChange}/>
                    <input type='submit' value={this.props.currentIndex == -1 ? 'Submit' : 'Update'}/>
                </form>

                <h2>List of transactions</h2>
                {this.props.data.length > 0 && (
                <table>
                    <thead>
                    <tr>
                        <th>Account</th>
                        <th>FSC</th>
                        <th>Name</th>
                        <th>Amount</th>
                    </tr>
                    </thead>
                    {this.props.data.map((item, i) => (
                    <tr key={i}>
                        <td>{item.accountNumber}</td>
                        <td>{item.fsc}</td>
                        <td>{item.name}</td>
                        <td>{item.amount}</td>
                        <td>
                        <button onClick={() => this.handleEdit(i)}>Edit</button>
                        <button onClick={() => this.handleDelete(i)}>Delete</button>
                        </td>
                    </tr>
                    ))}
                </table>
                )}
            </>
        )
    }
}

const mapStateToProps = state => {
    return{
        data: state.data
    }
}

const mapDispatchToProps = (dispatch) => {
  return {
    insertPayment: (data) => dispatch(insertPayment(data)),
    updatePayment: (data) => dispatch(updatePayment(data)),
    updateIndex: (data) => dispatch(updateIndex(data)),
    deletePayment: (data) => dispatch(deletePayment(data)),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(TransactionForm)