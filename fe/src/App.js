import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [number, setNumber] = useState('');
  const [result, setResult] = useState([]);

  const validateNumber = (number) => {
    return !isNaN(number) && Number.isInteger(parseFloat(number));
  };

  const handleChange = (e) => {
    setNumber(e.target.value);
  };

  const handleSubmit = async (url) => {
    if (validateNumber(number)) {
      try {
        const res = await axios.post(`http://127.0.0.1:5000${url}`, { number });
        setResult(res.data.triangle || res.data.odd_numbers || res.data.prime_numbers || []);
      } catch (err) {
        console.log(err);
      }
    } else {
      alert('Please enter a valid number');
    }
  };

  return (
    <div className="App">
      <form onSubmit={(e) => e.preventDefault()}>
        <input type="text" value={number} onChange={handleChange} placeholder="Input Angka"/>
        <br></br>
        <button type="button" onClick={() => handleSubmit('/generate_segitiga')}>
          Generate Segitiga
        </button>
        <button type="button" onClick={() => handleSubmit('/generate_ganjil')}>
          Generate Bilangan Ganjil
        </button>
        <button type="button" onClick={() => handleSubmit('/generate_prima')}>
          Generate Bilangan Prima
        </button>
      </form>
      <div className="result">
        <pre>{result}</pre>
      </div>
    </div>
  );
}

export default App;