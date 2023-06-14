import logo from './logo.svg';
import './App.css';
import React from 'react'

class FormComponent extends React.Component{

  constructor(props){
    super(props)

    this.state = {
      fname: '',
      lname: '',
      age: '',
      gender: '',
      destination: '',
      nuts: '',
      lactose: '',
      vegan: ''
    }
  }

  handleChange = (event) => {
    const value = (event.target.type == 'checkbox') ? event.target.checked : event.target.value
    this.setState({[event.target.name]:event.target.value})
  }

  changeDestination = (event) => {
    this.setState({destination: event.target.value })
  }

  handleSubmit = (event) => {
    event.preventDefault()
    const {fname, lname, age, gender, destination, nuts, lactose, vegan } = this.state
    console.log(nuts)
    console.log(lactose)
    const nutsRestriction = nuts ? 'Food restriction: nuts' : ''
    const lactoseRestriction = lactose ? 'Food restriction: lactose' : ''
    const veganRestriction = vegan ? 'Food restriction: vegan' : ''
    console.log(fname, lname, age, gender, destination, nutsRestriction, lactoseRestriction, veganRestriction)
  }

  render(){
    return(
      <>
        <h2>My form</h2>
        <form method='GET' onSubmit={this.handleSubmit}>
          <table>
            <tbody>
            <tr><td><input name='fname' size='50' placeholder='First name' onChange={this.handleChange}/> </td></tr>
            <tr><td><input name='lname' size='50' placeholder='Last name' onChange={this.handleChange}/></td></tr>
            <tr><td><input name='age' size='50' placeholder='Age' onChange={this.handleChange}/></td></tr>
            <tr><td><div onChange={this.handleChange}> <input type='radio' name='gender' value='male'></input>Male <input type='radio' name='gender' value='female'></input>Female</div></td></tr>
            {/* <tr><td align='left'><input type='radio' name='gender' value='male'></input>Male</td></tr>
            <tr><td align='left'><input type='radio' name='gender' value='female'></input>Female</td></tr> */}
            <tr><td align='left'><label htmlFor="destination">Choose your destination: </label><select name='destination' onChange={this.handleChange}>
              <option value='USA'>USA</option>
              <option value='Israel'>Israel</option>
              <option value='UK'>UK</option>
              <option value='Russia'>Russia</option>
              <option value='Japan'>Japan</option>
            </select></td></tr>
            <tr><td align='left'>Dietary restrictions:</td></tr>
            <tr><td align='left'><input type='checkbox' name='nuts' onChange={this.handleChange}/>Nuts free</td></tr>
            <tr><td align='left'><input type='checkbox' name='lactose' onChange={this.handleChange}/>Lactose free</td></tr>
            <tr><td align='left'><input type='checkbox' name='vegan' onChange={this.handleChange}/>Vegan</td></tr>
            <tr><td align='left'><input type="submit" value="Submit"/></td></tr>
            </tbody>
          </table>
        </form>
        <div id='form-result'>
          <h4>Form results: </h4>
          <p>First name: {fname}</p>
          <p>Last name: {lname}</p>
          <p>Age: {age}</p>
          <p>Destination: {destination}</p>
          <p>Food restrictions: {nuts}, {lactose}, {vegan}</p>
        </div>
      </>
    )
  }  
}

function App() {
  return (
    <div className="App">
      <FormComponent/>      
    </div>
  );
}

export default App;
