import React from 'react'

class Color extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            favoriteColor:'red',
            show: true
        }
    }

    shouldComponentUpdate(){
        return true //works as intended, switching blocks the update
    }

    render(){
        if (this.state.show == true){
            return(
                <>
                <header>My favorite color is {this.state.favoriteColor}</header>
                <button onClick={()=>{ this.setState({favoriteColor: 'blue'})}}>Change color</button>
                <div id='prev'></div>
                <div id="updated"></div>
                {this.props.children}
                <button onClick={() => { this.setState({show:false})}}>Delete header</button>
                </>
            )
        }
        else{
            return(
                <>
                <header>My favorite color is {this.state.favoriteColor}</header>
                <button onClick={()=>{ this.setState({favoriteColor: 'blue'})}}>Change color</button>
                <div id='prev'></div>
                <div id="updated"></div>
                <button onClick={() => { this.setState({show:false})}}>Delete header</button>
                </>
            )
        }
    }

    componentDidMount(){
        setTimeout(()=>{ this.setState({favoriteColor: 'yellow'})}, 5000)
    }

    getSnapshotBeforeUpdate(prevProps, prevState){
        const prev = document.getElementById('prev')
        prev.textContent = `Before the update the favorite was ${prevState.favoriteColor}`
    }

    componentDidUpdate(prevProps, prevState){
        if (prevState.favoriteColor !== this.state.favoriteColor) {
            const updated = document.getElementById('updated')
            updated.textContent = `The updated favorite is ${this.state.favoriteColor}`
        }
    }
}

export default Color