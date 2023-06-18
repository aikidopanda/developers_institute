import { useState } from "react";
import { connect } from "react-redux";
import { IncreaseCounter, DecreaseCounter } from "../redux/actions";


const Counter = (props) => {
    const [count, setCount] = useState(0)
    return(
        <>
            <button onClick={()=>props.increment()}>+</button>
            {props.count}
            <button onClick={()=>props.decrement()}>-</button>
        </>
    )
}

const mapStateToProps = state => {
    return{
        count:state.count// title: state.property_one
    }
}

const mapDispatchToProps = dispatch => {
    return{
        increment: () => dispatch(IncreaseCounter()),
        decrement: () => dispatch(DecreaseCounter())
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Counter)