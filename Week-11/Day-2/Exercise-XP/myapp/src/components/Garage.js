import React from "react";

class Garage extends React.Component{
    constructor(props){
        super(props)
    }
    render(){
        return(
            <div>
                Who lives in my { this.props.size } garage?
            </div>
        )
    }
}

export default Garage