import logo from './logo.svg';
import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom'
import "bootstrap/dist/css/bootstrap.min.css";
import ErrorBoundary from './components/ErrorBoundary';
// import jsonData from './ex2.json'
// import jsonData from './ex3.json'

let fetched // for exercise 4

class HomeScreen extends React.Component{
  constructor(){
    super()
  }

  render(){
    return(
      <h1>Home</h1>
    )
  }
}

class ProfileScreen extends React.Component{
  constructor(){
    super()
  }

  render(){
    return(
      <h1>Profile Screen</h1>
    )
  }
}

class Shop extends React.Component{
  constructor(){
    super()
  }

  render(){

    throw Error('An error has occurred')
    
    return(
      <>
      <h1>Shop</h1>
      </>
    )
  }
}

//Exercise 1
// function App() {
  // return (
  //     <Router>
  //     <div className="App">
  //       <nav className='navbar-nav navbar-brand'>
  //         <ul>
  //           <li className='nav-item'><NavLink to='/'>Home</NavLink></li>
  //           <li className='nav-item'><NavLink to='/profile'>Profile</NavLink></li>
  //           <li className='nav-item'><NavLink to='/shop'>Shop</NavLink></li>
  //         </ul>          
  //       </nav>
  //     </div>
  //     <Routes>
  //       <Route path='/' element={<ErrorBoundary><HomeScreen/></ErrorBoundary>}/>
  //       <Route path='/profile' element={<ErrorBoundary><ProfileScreen/></ErrorBoundary>}/>
  //       <Route path='/shop' element={<ErrorBoundary><Shop/></ErrorBoundary>}/>
  //     </Routes>
  //   </Router>   
  // );
// }

// Exercise 2
// function App() {
//   return (
//     <>
//     <h1>Hi! This is a title</h1><br/>
//     {jsonData.map(item=>(
//       <div key={item.id}>
//         <h3>{item.title}</h3>
//         <p>{item.content}</p>
//       </div>
//     ))} 
//     </> 
//   );
// }

// Exercise 3

// class Example1 extends React.Component{
//   constructor(){
//     super()
//   }

//   render(){
//     return(
//       <>
//       <ul>
//         {jsonData.SocialMedias.map((item, i)=>(
//           <li key={i}>{item}</li>
//         ))}
//       </ul>
//       </>
//     )
//   }
// }

// class Example2 extends React.Component{
//   constructor(){
//     super()
//   }
//   render() {
//     return (
//       <>
//         {jsonData.Skills.map((item, i) => (
//           <div key={i}>
//             <p>{item.Area}</p>
//             {/* <ul>
//               {item.Skillset.map((item, j) => (
//                 <li key={j}>{item.Name}</li> //gives me Cannot read properties of undefined (reading 'map'), dont know why
//               ))}
//             </ul> */}
//           </div>
//         ))}
//       </>
//     );
//   }
// }

// class Example3 extends React.Component{
//   constructor(){
//     super()
//   }

//   render(){
//     return(
//     <>
//       {jsonData.Experiences.map((item, i) => (
//         <div key={i}>
//           <img src={item.logo}/>
//           <p>{item.name}</p>
//           <p>{item.roles[0].title}</p>
//           <p>{item.roles[0].location}</p>
//           <p>{item.roles[0].description}</p>
//         </div>
//       ))}
//     </>
//     )
//   }
// }

// function App() {
//   return (
//     <>
//     <Example1/>
//     <Example2/>
//     <Example3/>
//     </> 
//   );
// }

//Exercise 4
const url = 'https://webhook.site/28d6acd1-b9c6-454c-b8bb-8cb379a1e35d'

//I dont understand why the body remains empty. Looks like I have to install some extra modules, but not sure
// Postman says my url is fine and Webhook sees my fetch requests made in this code so theoretically it should be ok

let requestBody = {
  key1: 'myusername',
  email: 'mymail@gmail.com',
  name: 'Isaac',
  lastname: 'Doe',
  age: 27
}

let response
async function fetcher(){
  try {
    response = await fetch(url, {
    method: 'POST',
    mode: 'no-cors',
    headers: {
      'Accept': 'application/json',
      'Content-type': 'application/json' 
    },
    body: JSON.stringify(requestBody)
  })
  console.log(response) 
  }
  catch(error){
    console.log(error)
  }
}

function showData(){
  console.log(response)
}


function App() {
  fetcher()
  return (
    <>
    <button onClick={showData}>Show Data</button>
    </> 
  );
}

export default App;
