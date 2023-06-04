
import './App.css';

import { useState, useEffect } from 'react'

function App() {

  const [ data, setData ] = useState([])
  const [ dataTest, setDataTest ] = useState([])
  const [ status, setStatus ] = useState(null)
  const [ temp, setTemp ] = useState(20)

  useEffect(() => {

    const fetchData = async () => {
      const res = await fetch('http://localhost:5000/get_data');
      const data1 = await res.json()

      setData(data1)
      console.log(data1);
    }

    const fetchStatus = async () => {
      const res = await fetch("http://localhost:5000/get_status");
      const data1 = await res.json();

      setStatus(data1);
      console.log(data1);
    }

    fetchData();
    fetchStatus();
  }, [])

  const handleButton = async () => {
      const res = await fetch('http://localhost:5000/get_data');
      const data2 = await res.json()

      setDataTest(data2)
      console.log(data2);
  }

  const handleOff = async () => {
    // setStatus(0)
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

  const handleOn = async () => {
    // setStatus(1)
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

  const handlePLus = () => {
    setTemp(temp + 1)
  }

  const handleMinus = () => {
    setTemp(temp - 1)
  }

  const handleSet = () => {
    console.log(temp);
  }
 
  return (
    <div className="App">
      <h1 className='text-green-500 text-4xl font-semibold'>Hello</h1>
      <div>
        {data.map((el) => (
          <div key={el.id}>
            <p>{el.temperature}</p>
            <p>{el.humidity}</p>
          </div>
        ))}
      </div>

      <div>
        <button className="bg-slate-800 text-white p-2 rounded-md" onClick={handleButton}>Incarca</button>
          <div>
            {dataTest.length === 0 ? <h1>Nu avem date</h1> : (
              <div>
                {data.map((el) => (
                  <div key={el.id}>
                    <p>{el.temperature}</p>
                    <p>{el.humidity}</p>
                  </div>
                ))}
              </div>
            )}
          </div>
      </div>
      <div>
        {status === 1 ? (<div>
            <h2>The heating is ON</h2>
            <button className="bg-red-800 text-white p-2 rounded-md" onClick={handleOff}>Off</button>
          </div>)
           : (<div>
                <h2>The heating is OFF</h2>
                <button className="bg-green-700 text-white p-2 rounded-md" onClick={handleOn}>On</button>
              </div>)}
      </div>

      <div>
        <h2>Temp: {temp}</h2>
        <button onClick={handlePLus} className="bg-slate-800 text-white p-2 rounded-md m-4">+</button>
        <button onClick={handleMinus} className="bg-slate-800 text-white p-2 rounded-md m-4">-</button>
        <button onClick={handleSet} className="bg-slate-800 text-white p-2 rounded-md m-4">Set</button>
      </div>
    </div>
  );
}

export default App;
