import logo from './logo.svg';
import './App.css';
import React from 'react'
import quotes from './quotes';

const divColors = ['lightred', 'azure', 'white', 'gold', 'yellow', 'lightblue', 'lightgreen', 'orange', 'pink']
const bodyColors = ['blue', 'purple', 'maroon', 'brown', 'black', 'darkviolet', 'darkblue', 'darkgreen', 'olivegreen']

class QuoteBlock extends React.Component{
  constructor(){
    super()
    this.state = {
      index: Math.floor(Math.random() * quotes.length),
      colorIndex: Math.floor(Math.random() * divColors.length)
    }
  }

  changeBodyColor = () => {
    document.body.style.backgroundColor = bodyColors[this.state.colorIndex];
  }

  newQuote = () => {
    quotes.splice(this.state.index, 1)
    this.setState({
      index: Math.floor(Math.random() * quotes.length),
      colorIndex: Math.floor(Math.random() * divColors.length)
    })
    this.changeBodyColor()
  }

  render(){
    this.changeBodyColor()
    return(
      <div style = {{backgroundColor: divColors[this.state.colorIndex], color: bodyColors[this.state.colorIndex]}} id='quote-container'>
        <h2>{quotes[this.state.index].quote}</h2>
        <p style={{color: bodyColors[this.state.colorIndex]}}>{quotes[this.state.index].author}</p>
        <button style = {{ backgroundColor: bodyColors[this.state.colorIndex], color: 'cyan', width: '7.5vw', marginLeft: '42vw', marginBottom: '1vh', marginRight: '1vw'}}onClick={this.newQuote}>New Quote</button>
      </div>
    )
  }
}

function App() {
  return (
    <div>
      <QuoteBlock/>
    </div>
  );
}

export default App;
