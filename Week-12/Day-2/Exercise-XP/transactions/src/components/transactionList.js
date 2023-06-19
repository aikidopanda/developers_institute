import React from 'react'
import { connect } from 'react-redux'
import { insertPayment } from '../actions/actions'

class TransactionList extends React.Component{
    constructor(props){
        super(props)
    }

    render() {
        return (
          <div>
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
                      <button>Edit</button>
                      <button>Delete</button>
                    </td>
                  </tr>
                ))}
              </table>
            )}
          </div>
        );
      }
}

const mapStateToProps = state => {
    return{
        data: state.data
    }
}

const mapDispatchToProps = (dispatch) => {
  return {
    InsertPayment: (data) => dispatch(insertPayment(data)),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(TransactionList)