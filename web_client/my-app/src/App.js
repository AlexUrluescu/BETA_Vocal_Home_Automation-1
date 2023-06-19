import "./App.css";

//theme
import "primereact/resources/themes/lara-light-indigo/theme.css";     
    
//core
import "primereact/resources/primereact.min.css";
import { Button } from 'primereact/button';

import { SelectButton } from 'primereact/selectbutton';
              
// import dotenv from "dotenv";

// dotenv.config()

// const url = process.env.SERVER_URL 

import { useState, useEffect } from "react";

const url = "https://smarthome-dowt.onrender.com";

function App() {
  // eslint-disable-next-line
  const [tempHome, setTempHome] = useState(0);
  const [humHome, setHumHome] = useState(0);
  const [statusHeating, setStatusHeating] = useState(0);
  const [heatingTemp, setHeatingTemp] = useState(0);

  const options = ['Off', 'On'];
  const [value, setValue] = useState(options[0]);

  useEffect(() => {
    // get all the temperatures and humiditys
    const fetchData = async () => {
      try {
        const res = await fetch(`${url}/datasenzors`);
        const data1 = await res.json();

        setTempHome(data1[0].temperature);
        setHumHome(data1[0].humidity)
        console.log(data1);
      } catch (error) {
        console.log(error);
      }
    };

    // get the status of the heating system
    const fetchStatus = async () => {
      try {
        const res = await fetch(`${url}/heatingstatus`);
        const data1 = await res.json();

        setStatusHeating(data1[0]);
        console.log(data1);
      } catch (error) {
        console.log(error);
      }
    };

    // get the temperature of the heating system
    const fetchHeatingTemp = async () => {
      try {
        const res = await fetch(`${url}/heatingtemp`);
        const data1 = await res.json();

        // setFinalTemp(data1);
        setHeatingTemp(data1[0]);
        console.log(data1);
      } catch (error) {
        console.log(error);
      }
    };

    const fetchTest = async () => {
      try {
        const res = await fetch("https://192.168.1.101:5000/get_data")
        const data = await res.json()

        console.log(data);
        
      } catch (error) {
        console.log(error);
      }
    }

    fetchData();
    fetchStatus();
    fetchHeatingTemp();
    // fetchTest();
  }, []);

  const handleChange = async (e) => {
      setValue(e.value)
      console.log(e.value);

      if(e.value === 'On'){
        const status = 1;

        try {
          const data = await fetch(`http://localhost:5000/changestatus/${statusHeating._id}`, {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json'
          },
            body: JSON.stringify({ status })
          });
    
          const res = await data.json();
    
          console.log(res);
          if(res.message === "ok"){
            setStatusHeating({...statusHeating, status: 1})
          }
          // setStatus(data.status);
        } catch (error) {
          console.log(error);
        }
       

      }

      else if(e.value === "Off"){
        try {
          const status = 0;
          const data = await fetch(`http://localhost:5000/changestatus/${statusHeating._id}`, {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json'
          },
            body: JSON.stringify({ status })
          });
    
          const res = await data.json();
    
          console.log(res);
          if(res.message === "ok"){
            setStatusHeating({...statusHeating, status: 0})
          }
          
        } catch (error) {
          console.log(error);
        }
      }
    
  }

  // turn OFF the heating system
  const handleOff = async () => {

    const status = 0;

    try {
      const data = await fetch(`${url}/changestatus/${statusHeating._id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
      },
        body: JSON.stringify({ status })
      });

      const res = await data.json();

      console.log(res);
      if(res.message === "ok"){
        setStatusHeating({...statusHeating, status: 0})
      }
      // setStatus(data.status);
    } catch (error) {
      console.log(error);
    }
  };

  // turn ON the heating system
  const handleOn = async () => {
    const status = 1;

    try {
      const data = await fetch(`${url}/changestatus/${statusHeating._id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
      },
        body: JSON.stringify({ status })
      });

      const res = await data.json();

      console.log(res);
      if(res.message === "ok"){
        setStatusHeating({...statusHeating, status: 1})
      }
      // setStatus(data.status);
    } catch (error) {
      console.log(error);
    }

  };

  // increment the value of the temperature
  const handlePLus = () => {
  
    const temperature = heatingTemp.temperature;
    setHeatingTemp({...heatingTemp, temperature: temperature + 1})

  };

  // decrement the value of the temperature
  const handleMinus = () => {

    const temperature = heatingTemp.temperature;
    setHeatingTemp({...heatingTemp, temperature: temperature - 1});


  };

  // set the final temperature
  const handleSet = async () => {

    const temperature = heatingTemp.temperature;

    try {
      const data = await fetch(`${url}/changeheatingtemp/${heatingTemp._id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
      },
        body: JSON.stringify({ temperature })
      });

      const res = await data.json();

      console.log(res);
      if(res.message === "ok"){
        setHeatingTemp({...heatingTemp, temperature: temperature})
      }

    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="App">
      <div className="bg-slate-700 text-white flex justify-center items-center p-10 pb-20 sm:h-screen">
        <div className="p-3 w-screen">
          <div className="p-3 mb-6">
            <h1 className="text-6xl font-semibold">Smart Heating</h1>
            <Button label="Check"/>
            <SelectButton value={value} onChange={handleChange} options={options} />
            {value === "On" ? <h2>On</h2> : <h2>Off</h2>}
          </div>
          <div className="flex flex-col gap-8 sm:flex-row">
            <div className="w-full p-5 sm:w-2/4 flex flex-col items-center justify-center">
              <h1 className="mb-10 mt-10 text-3xl font-semibold">
                Home's data
              </h1>

              <div>
                <div className="bg-gray-900 h-40 w-40 flex justify-center items-center rounded-full mb-4 text-6xl border-4 border-white-300">
                  {tempHome}
                  <sup className="text-lg">° C</sup>
                </div>
                <div className="bg-gray-900 h-40 w-40 flex justify-center items-center rounded-full text-6xl border-4 border-white-300">
                  {humHome}
                  <sup className="text-lg">%</sup>
                </div>
              </div>
            </div>
            <div className="w-full border-x-0 border-white-500 border-t-2 border-white-500 p-5 sm:w-2/4 sm:border-l-4 border-white-500 sm:border-t-0">
              <div>
                {statusHeating.status === 1 ? (
                  <h1 className="bg-green-200 w-80 m-auto mt-10 mb-10 p-3 rounded-full border-4 border-green-500 text-black">
                    The heating system is ON
                  </h1>
                ) : (
                  <h1 className="bg-red-200 w-80 m-auto mt-10 mb-10 p-3 rounded-full border-4 border-red-500 text-black">
                    The heating system is OFF
                  </h1>
                )}
              </div>
              <div className="flex justify-center items-center gap-4">
                <div>
                  {statusHeating.status === 1 ? (
                    <button
                      className="bg-red-800 text-white text-xl flex flex-col items-center justify-center rounded-full m-4 h-16 w-16 border-4 border-white-300"
                      onClick={handleOff}
                    >
                      Off
                    </button>
                  ) : (
                    <button
                      className="bg-green-700 text-white text-xl flex flex-col items-center justify-center rounded-full m-4 h-16 w-16 border-4 border-white-300"
                      onClick={handleOn}
                    >
                      On
                    </button>
                  )}
                </div>

                <div className="bg-gray-900 h-40 w-40 flex justify-center items-center rounded-full text-6xl border-4 border-white-300">
                  {heatingTemp.temperature} <sup className="text-lg"> ° C</sup>
                </div>
                <div className="flex flex-col">
                  <button
                    onClick={handlePLus}
                    className="btn"
                  >
                    +
                  </button>
                  <button
                    onClick={handleSet}
                    className="bg-amber-400 text-white text-xl flex flex-col items-center justify-center rounded-full m-4 h-16 w-16 border-4 border-white-300"
                  >
                    Set
                  </button>
                  <button
                    onClick={handleMinus}
                    className="btn"
                  >
                    -
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
