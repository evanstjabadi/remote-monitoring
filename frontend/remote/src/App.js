import React, { Component } from 'react'
import './App.css'
import Graphs from './Graphs'

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>Welcome to Remote Monitoring</h2>
        </div>
        <p className="App-intro">
          There's a rasperry pi connected to the internet somewhere loading data
          for the graph below
        </p>
        <div className="Graph-container">
          <Graphs className="Graph" />
        </div>
      </div>
    )
  }
}

export default App
