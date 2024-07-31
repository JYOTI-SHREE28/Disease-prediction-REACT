import React, { useState } from "react";
import axios from 'axios';
import './App.css';

function Form() {
  const [inputData, setInputData] = useState({ symptoms: "" });
  const [result, setResult] = useState("");

  function handleData(e) {
    setInputData({ ...inputData, [e.target.name]: e.target.value });
    console.log(inputData);
  }

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      const response = await axios.post('/predict', inputData);
      setResult(response.data.disease);
    } catch (error) {
      console.error("There was an error making the request", error);
      setResult("Error occurred during prediction");
    }
  }

  return (
    <div id="container">
      <h1>SYMPTOM SENSE</h1>
      <form id="symptomForm" onSubmit={handleSubmit}>
        <label htmlFor="symptom">Enter your symptoms:</label>
        <div>
          <input
            type="text"
            name="symptoms"
            value={inputData.symptoms}
            onChange={handleData}
          />
        </div>
        <button type="submit">Predict Disease</button>
      </form>
      <div id="result">{result}</div>
    </div>
  );
}

export default Form;
