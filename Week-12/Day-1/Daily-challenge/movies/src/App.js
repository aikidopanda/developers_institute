import logo from './logo.svg';
import './App.css';
import MovieList from './components/movielist';
import MovieSelected from './components/moviedetails';

function App() {
  return (
    <div className="App">
      <MovieList/>
      <MovieSelected/>
    </div>
  );
}

export default App;
