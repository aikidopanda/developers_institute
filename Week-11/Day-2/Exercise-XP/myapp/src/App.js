import logo from './logo.svg';
import './App.css';
import Car from './components/Car';
import Events from './components/Events';
import Phone from './components/Phone';
import Color from './components/Color';

const carInfo = {
  name: 'Ford',
  model: 'Mustang'
}

//Exercise 1
// function App() {
//   return (
//     <div className="App">
//       <Car model={carInfo.model}/>
//     </div>
//   );
// }

// //Exercise 2
// function App() {
//   return (
//     <div className="App">
//       <Events/>
//     </div>
//   );
// }

//Exercise 3
// function App() {
//   return (
//     <div className="App">
//       <Phone/>
//     </div>
//   );
// }

//Exercise 4
function App() {
  return (
    <div className="App">
      <Color/>
    </div>
  );
}

export default App;


