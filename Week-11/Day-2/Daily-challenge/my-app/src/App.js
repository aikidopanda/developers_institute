import logo from './logo.svg';
import './App.css';
import React from 'react';

class Voting extends React.Component{
  constructor(props){
    super(props)
    this.state = {
      languages : [
          {name: "Php", votes: 0},
          {name: "Python", votes: 0},
          {name: "JavaSript", votes: 0},
          {name: "Java", votes: 0}
      ]
    }
  }

  addVote = (index) => {
    this.setState((prevState) => {
      const updatedLanguages = [...prevState.languages];
      updatedLanguages[index] = {
        ...updatedLanguages[index],
        votes: updatedLanguages[index].votes + 1
      };
  
      return {
        languages: updatedLanguages
      };
    });
  };

  render() {
    return (
      <>
        {this.state.languages.map((language, index) => (
          <div key={index}>
            {language.votes} {language.name} <button onClick={() => this.addVote(index)}>Click here!</button>
          </div>
        ))}
      </>
    );
  }
}



function App() {
  return (
    <div className="App">
      <Voting/>
    </div>
  );
}

export default App;
