import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Range from './Range/Range.js';
import Cards from './Cards/Cards.js';
import MainContainer from './MainContainer/MainContainer.js';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Cards/>
        <MainContainer/>
      </div>
    );
  }
}

export default App;
