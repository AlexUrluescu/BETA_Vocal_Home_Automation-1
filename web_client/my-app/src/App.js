
import './App.css';

import { useState, useEffect } from 'react'

function App() {

  const [ data, setData ] = useState([])
  const [ status, setStatus ] = useState(null)
  const [ recentData, setRecentData ] = useState({})

  const [ finalTemp, setFinalTemp ] = useState()
  const [ temp, setTemp ] = useState(null)


  useEffect(() => {

    // get all the temperatures and humiditys
    const fetchData = async () => {
      try {
        const res = await fetch('http://localhost:5000/get_data');
        const data1 = await res.json()
  
        setData(data1)
        console.log(data1);
        
      } catch (error) {
        console.log(error);
      }
    }

    // get the status of the heating system
    const fetchStatus = async () => {
      try {
        const res = await fetch("http://localhost:5000/get_status");
        const data1 = await res.json();
  
        setStatus(data1);
        console.log(data1);
        
      } catch (error) {
        console.log(error);
      }

    }

    // get the temperature of the heating system
    const fetchHeatingTemp = async () => {
      try {
        const res = await fetch("http://localhost:5000/get_heating_temp");
        const data1 = await res.json();

        setFinalTemp(data1);
        setTemp(data1)
        console.log(data1);
        
      } catch (error) {
        console.log(error);
      }
    }

    // get the recent temperature and humidty of the sensors
    const fetchRecentTemp = async () => {
      try {
        const res = await fetch("http://localhost:5000/get_recent_temp");
        const data1 = await res.json();

        setRecentData(data1);
        console.log(data1);
        
      } catch (error) {
        console.log(error);
      }
    }

    fetchData();
    fetchStatus();
    fetchHeatingTemp();
    fetchRecentTemp();
  }, [])


  // turn OFF the heating system
  const handleOff = async () => {
    const options = {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      }
    }

    try {
        const res = await fetch("http://localhost:5000/turn_off_status", options);
        const data = await res.json();

        console.log(data);
        setStatus(data.status)
        
    } catch (error) {
        console.log(error);
    }
  }


  // turn ON the heating system
  const handleOn = async () => {
    const options = {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      }
    }

    try {
        const res = await fetch("http://localhost:5000/turn_on_status", options);
        const data = await res.json();

        console.log(data);
        setStatus(data.status)
        
    } catch (error) {
        console.log(error);
    }
  }


  // increment the value of the temperature
  const handlePLus = () => {
    setTemp(temp + 1)
  }

  // decrement the value of the temperature
  const handleMinus = () => {
    setTemp(temp - 1)
  }

  // set the final temperature
  const handleSet = async () => {
    console.log(temp);

    const value_temp = {
      value: temp
    }

    const options = {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(value_temp)
    }

    try {
        const res = await fetch("http://localhost:5000/set_heating_temp", options);
        const data = await res.json();

        console.log(data);
        setFinalTemp(data.temperature)
        
    } catch (error) {
        console.log(error);
    }
  }
 
  return (
    <div className="App">
      <div className="bg-black text-white flex justify-center items-center p-5">
        <div className="w-2/4 border-r border-r-white p-3">
          <div><h1 className="text-4xl font-semibold">Smart Heating</h1></div>
          <div className="bg-white mt-10 text-black">
            <h1>Home's temperature: {recentData.temperature} ° C</h1>
            <h1>Home's humidity: {recentData.humidity}</h1>
          </div>
          <div>
            <div className="bg-white text-black mt-10">
              {status === 1 ? (<div>
                <h2 className="text-green-700 font-semibold">The heating is ON</h2>
                <button className="bg-red-800 text-white p-2 rounded-xl mt-5" onClick={handleOff}>Off</button>
              </div>)
              : (<div>
                  <h2 className="text-red-700 font-semibold">The heating is OFF</h2>
                  <button className="bg-green-700 text-white p-2 rounded-xl mt-5" onClick={handleOn}>On</button>
                </div>)}
            </div>
          </div>
          <div className="bg-white mt-10 text-black p-5">
            <h2>Heating system settings</h2>
            <h2>The temperature of the heating system: {finalTemp}</h2>
            <h2 className="mt-5">Set temperature: <span className="bg-gray-600 text-white p-1">{temp} ° C</span></h2>
            <button onClick={handlePLus} className="bg-slate-800 text-white p-2 rounded-xl m-4 h-10 w-10">+</button>
            <button onClick={handleMinus} className="bg-slate-800 text-white p-2 rounded-xl m-4 h-10 w-10">-</button>
            <button onClick={handleSet} className="bg-slate-800 text-white p-2 rounded-xl m-4 h-10 w-13">Set</button>
          </div>
        </div>
        <div className="w-2/4">Chart</div>
      </div>
    </div>
  );
}

export default App;
