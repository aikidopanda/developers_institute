import logo from './logo.svg';
import './App.css';
import { connect } from 'react-redux';
import React from 'react'
import Test from './components/test'
// import { changePropOne } from './redux/actions';
import Counter from './components/Counter';

function App() {
  return (
    <div className="App">
      <Counter count='0'/>
    </div>
  );
}

const mapStateToProps = (state) => {
  console.log('store=>',state)
  return {

  }
}

export default connect(mapStateToProps, mapStateToProps)(App);
