import React from 'react'
import { connect } from "react-redux";
import { selectMovie } from '../actions/actions';

class MovieList extends React.Component{
    constructor(props){
        super(props)
    }

    render() {
        return (
          <div>
            <h2>Movie List</h2>
            {this.props.movies.map((item, i) => (
              <div key={i}>
                {item.title}
                <button onClick={()=>this.props.selectMovie(item)}>details</button>
              </div>
            ))}
          </div>
        );
    }
}

const mapStateToProps = state => {
    return{
        movies: state.moviesReducer.movies
    }
}

const mapDispatchToProps = (dispatch) => {
  return {
    selectMovie: (movie) => dispatch(selectMovie(movie)),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(MovieList)
