import React from 'react'
import Garage from './Garage'

class Car extends React.Component{
    constructor(props) {
        super(props)
        this.state = { color: 'red'}
    }
    render(){
        return(
            <header>
                <Garage/>
                <p>This car is { this.state.color} { this.props.model }</p>
            </header>
        )
    }
}

export default Car