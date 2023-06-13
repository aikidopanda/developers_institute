import React from 'react'
class ErrorBoundary extends React.Component {
    constructor(){
        super()
        this.state = {
            hasError: false,
            error: null,
        }
    }
  
    componentDidCatch(error){
        this.setState({hasError: true, error:error})
    }
  
    render(){
        if(this.state.hasError){
            return(
                <>
                Something is wrong, we are fixing the problem
                </>
            )
        }
        return this.props.children
    }
  }

export default ErrorBoundary