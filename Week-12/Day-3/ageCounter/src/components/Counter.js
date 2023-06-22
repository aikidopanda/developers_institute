import { connect } from "react-redux";
import { IncreaseAge, DecreaseAge } from "../redux/actions";


const ageCounter = (props) => {
    return(
        <>
            <span>Your age: {props.age} </span>
            <button onClick={()=>props.increment()}>Age Up</button>
            <button onClick={()=>props.decrement()}>Age Down</button>
        </>
    )
}

const mapStateToProps = state => {
    return{
        age:state.age// title: state.property_one
    }
}

const mapDispatchToProps = dispatch => {
    return{
        increment: () => dispatch(IncreaseAge()),
        decrement: () => dispatch(DecreaseAge()),
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(ageCounter)