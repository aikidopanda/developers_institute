import logo from './logo.svg';
import './App.css';
import React from 'react'
import ErrorBoundary from './components/ErrorBoundary';
import Color from './components/Color';

class BuggyCounter extends React.Component{
  constructor(){
      super()
      this.state = {
          count:0
      }
  }

  handleClick= () => {
      this.setState({count: this.state.count + 1})
  }

  render(){
      if(this.state.count >= 5){
          throw Error('I crashed!')
      }
      return(
          <>
          {this.state.count}
          <button onClick={this.handleClick}>Add</button>
          </>
      )
  }
}

class Child extends React.Component{
  constructor(){
    super()
  }

  componentWillUnmount(){
    alert('Child is unmounted!')
  }

  render(){
    return(
      <h3>Hello World!</h3>
    )   
  }
}

//Exercise 1
//Simulation 1
// function App() {
//   return (
//     <div className="App">
//       <ErrorBoundary>
//         <BuggyCounter/>
//         <BuggyCounter/>
//       </ErrorBoundary>
//     </div>
//   );
// }

//Simulation2
// function App() {
//   return (
//     <div className="App">
//       <ErrorBoundary>
//         <BuggyCounter/>
//       </ErrorBoundary>
//       <ErrorBoundary>
//         <BuggyCounter/>
//       </ErrorBoundary>
//     </div>
//   );
// }

//Simulation 3
// function App() {
//   return (
//     <div className="App">
//       <BuggyCounter/>
//     </div>
//   );
// }

//Exercise 2

// function App() {
//   return (
//     <div className="App">
//       <Color/>
//     </div>
//   );
// }

//Exercise 3
function App() {
  return (
    <div className="App">
      <Color>
      <Child/>
      </Color>
    </div>
  );
}




export default App;
