import React from 'react'
import { connect } from "react-redux";
import { selectMovie } from '../actions/actions';
import selectMovieReducer from '../reducers/reducers'

class MovieSelected extends React.Component{
    constructor(props){
        super(props)
    }

    render(){
        console.log(this.props)
        return(
            <>
                <h2>Selected movie:</h2>
                <p>Title: {this.props.movie ? this.props.movie.title : ''}</p>
                <p>Release date: {this.props.movie ? this.props.movie.releaseDate : ''}</p>
                <p>Rating: {this.props.movie ? this.props.movie.rating : ''}</p>
            </>
        )
    }
}

const mapStateToProps = state => {
    return{
        movie: state.selectMovieReducer.movie
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
      selectMovie: (movie) => dispatch(selectMovie(movie)),
    };
  };

export default connect(mapStateToProps, mapDispatchToProps)(MovieSelected)
