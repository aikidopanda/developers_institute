import React from 'react'

class Color extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            favoriteColor:'red'
        }
    }

    render(){
        return(
            <>
        <header>My favorite color is {this.state.favoriteColor}</header>
        <button onClick={()=>{ this.setState({favoriteColor: 'blue'})}}>Change color</button>
        </>
        )
    }

    componentDidMount(){
        setTimeout(()=>{ this.setState({favoriteColor: 'yellow'})}, 5000)
    }
}

export default Color