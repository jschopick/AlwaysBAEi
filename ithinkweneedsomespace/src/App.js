import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>I'm sorry, I think we need some space...</h1>
        <svg class="heart" viewBox="0 0 32 29.6">
          <path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2
            c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/>
        </svg> 
        <p></p>
        <p>It's not you - it's me. Really! You'll always be BAE in my eyes. <br></br>
        You still don't believe me? I even spent all weekend creating a <br></br>
        computer vision program that tells you what I think of you. At least <br></br>
        take a look at <a className="App-link" href="https://devpost.com/software/alwaysbaei">AlwaysBAEi</a>! :)</p>
      </header>
    </div>
  );
}

export default App;