import { connect } from "react-redux";

const Test = (props) => {
    return(
        <>
        <h1>{props.title}</h1>
        <button
        onClick = {()=>props.setTitle('Test Title')}>
            Change Title
        </button>
        </>
    )
}

const mapStateToProps = state => {
    return{
        title: state.property_one
    }
}

export default connect(mapStateToProps)(Test)