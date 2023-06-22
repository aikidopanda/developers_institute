import logo from './logo.svg';
import './App.css';
import React from 'react'
import { createContext, useContext } from 'react';


const key = 'R2amgXEMLdmVr9dGwPIIQOB1AUygg2SL'

const MyContext = createContext()

class CityWeather extends React.Component{
  constructor(){
    super()
    this.state = {
      userInput: '',
      cities: []
    }
  }

  componentDidUpdate(){
    if (this.state.cities.length == 0){
        return async () => {
          const url = `http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=${key}&q=${this.state.userInput}`
          let response = await fetch(url)
          let responseJson = await response.json()
          this.setState({...this.state, cities: [...responseJson]})
        }
    }
    
  }

  handleSearch(event){
    this.setState({...this.state, userInput: event.target.value})

  }

  render(){
    return(
      <>
        <input placeholder='Enter the name of the city' onChange={handleSearch}/>
      </>
    )   
  }
}



function App() {
  return (
    <div className="App">
      <CityWeather/>
    </div>
  );
}

export default App;
