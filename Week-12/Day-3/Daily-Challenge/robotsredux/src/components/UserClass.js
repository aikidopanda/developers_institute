import React from 'react'
import {connect} from 'react-redux'
import { searchInput } from '../redux/actions'

class UserClass extends React.Component{

  state = {
    search:''
  }


  handleChange = (event) => {
    this.setState()
  }

  render(){
    const {list} = this.props
    
    return(
      <div>
        <input type='search' placeholder='Start searching'/>
        {
          list.map((robot) => (
            <div className="tc grow bg-light-green br3 pa3 ma2 dib bw2 shadow-5" key={robot.id}>
              <img src={`https://robohash.org/${robot.id}`} alt="Robot" />
              <h2>{robot.name}</h2>
              <p>{robot.username}</p>
              <p>{robot.email}</p>
              </div>
          ))
        }
      </div>
    )
  }
}

export default UserClass
