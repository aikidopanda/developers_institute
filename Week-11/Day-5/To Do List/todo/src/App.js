import './App.css';
import React from 'react'


class AddTodo extends React.Component{
  constructor(){
    super()

    this.state = {
      todos:[],
      value: ''
    }
  }

  handleSubmit = (event) => {
    event.preventDefault()
    const newItem = {
      id: this.state.todos.length,
      text: event.target.todo.value
    }
    this.setState(prevState => ({
      todos: [...prevState.todos, newItem]
    }))
  }

  render(){
    return(
      <>
      <form onSubmit={this.handleSubmit}>
        Enter a new todo: <input name='todo'></input>
        <input type='submit' value='Add new todo'></input>
      </form>
      {this.state.todos.map((item) => (
         <div className='todo' key={item.id}>
          {item.text}<br/>
          <button className='addtodo' key={item.id} onClick={
            ()=>{
              const indexToRemove = this.state.todos.findIndex(itemRem=>itemRem.id == item.id)
              this.state.todos.splice(indexToRemove,1);
              this.setState({value:''});
            }
          }>
            Remove
          </button>
        </div>
      ))}
      </>
    )
  }
}


function App() {
  return (
    <div className="App">
        <AddTodo/>
    </div>
  );
}

export default App;
