import React from 'react'

class ErrorBoundary extends React.Component{
    constructor(){
        super()
        this.state = {
            hasError: false
        }
    }

    componentDidCatch(){
        this.setState({hasError: true})
    }

    render(){
        if (this.state.hasError == true){
            return(
                <>
                <h1>An error has occurred</h1>
                </>
            )
        }
        return this.props.children
    }
}

export default ErrorBoundary