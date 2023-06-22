import { connect } from "react-redux";
import { IncreaseCounter, DecreaseCounter, IncrementIfOdd, IncrementAsync } from "../redux/actions";


const Counter = (props) => {
    return(
        <>
            {props.count}
            <button onClick={()=>props.increment()}>+</button>
            <button onClick={()=>props.decrement()}>-</button>
            <button onClick={()=>props.incrementIfOdd()}>Increment If Odd</button>
            <button onClick={()=>props.incrementAsync()}>Increment Async</button>
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
        decrement: () => dispatch(DecreaseCounter()),
        incrementIfOdd: () => dispatch(IncrementIfOdd()),
        incrementAsync: () => dispatch(IncrementAsync())
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Counter)