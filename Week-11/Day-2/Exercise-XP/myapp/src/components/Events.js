import React from "react"

class Events extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            isToggleOn: 'ON'
        }
    }

    clickMe = () =>{
        alert('I was clicked!')
    }

    handleKeyDown = (event) =>{
        if (event.keyCode == 13){
            alert('You pressed the Enter key!')
        }
    }

    toggler = () => {
        if (this.state.isToggleOn == 'ON'){
            this.setState({isToggleOn: 'OFF'})
        }
        else{
            this.setState({isToggleOn: 'ON'})
        }
    }

    render(){
        return(
            <>
            <input onKeyDown={this.handleKeyDown} placeholder="Type something"/>
            <button type="button" onClick={this.clickMe}>Click Me</button>
            <button type="button" onClick={this.toggler}>{this.state.isToggleOn}</button>
            </>
        )
    }
}

export default Events