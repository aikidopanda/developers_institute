import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import FavoriteColors from './colors';
import MyComp from './ex4';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));

//Exercise 1
// const element = React.createElement('h1', null, 'I dont use JSX'); // only for exercise 1
// root.render(
//   <React.StrictMode>
//     { element } 
//   </React.StrictMode>
// );

//Exercise 2
// const HelloWorld = () => {

//   let msg = 'Hello World!'
//   const myelement = 'I love JSX'
//   const sum = 5 + 5

//   return (
//     <>
//     <h1>{ msg }</h1>
//     <h2> { myelement }</h2>
//     <p>React is {sum} times better with JSX</p>
//     </>
//   )
// }
// root.render(
//   <React.StrictMode>
//     <HelloWorld/> 
//   </React.StrictMode>
// );

//Exercise 3
// const user = {
//   firstName: 'Bob',
//   lastName: 'Dylan',
//   favAnimals : ['Horse','Turtle','Elephant','Monkey']
// };
// const Person = () => {
//   return (
//     <>
//       <h3>{user.firstName}</h3>
//       <h3>{user.lastName}</h3>
//     </>   
//   )
// }
// root.render(
//   <React.StrictMode>
//     <Person />
//     <FavoriteColors animals = {user.favAnimals}/> 
//   </React.StrictMode>
// );

//Exercise 4

root.render(
  <React.StrictMode>
    <MyComp /> 
  </React.StrictMode>
);






// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
// export default Person
