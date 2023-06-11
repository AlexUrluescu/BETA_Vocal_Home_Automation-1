import "./App.css";
// import dotenv from "dotenv";

// dotenv.config()

// const url = process.env.SERVER_URL 

import { useState, useEffect } from "react";

const url = "http://192.168.1.101:5000";

function App() {
  // eslint-disable-next-line
  const [data, setData] = useState([]);
  const [status, setStatus] = useState(null);
  const [recentData, setRecentData] = useState({});

  // eslint-disable-next-line
  const [finalTemp, setFinalTemp] = useState();
  const [temp, setTemp] = useState(null);

  useEffect(() => {
    // get all the temperatures and humiditys
    const fetchData = async () => {
      try {
        const res = await fetch(`${url}/get_data`);
        const data1 = await res.json();

        setData(data1);
        console.log(data1);
      } catch (error) {
        console.log(error);
      }
    };

    // get the status of the heating system
    const fetchStatus = async () => {
      try {
        const res = await fetch(`${url}/get_status`);
        const data1 = await res.json();

        setStatus(data1);
        console.log(data1);
      } catch (error) {
        console.log(error);
      }
    };

    // get the temperature of the heating system
    const fetchHeatingTemp = async () => {
      try {
        const res = await fetch(`${url}/get_heating_temp`);
        const data1 = await res.json();

        setFinalTemp(data1);
        setTemp(data1);
        console.log(data1);
      } catch (error) {
        console.log(error);
      }
    };

    // get the recent temperature and humidty of the sensors
    const fetchRecentTemp = async () => {
      try {
        const res = await fetch(`${url}/get_recent_temp`);
        const data1 = await res.json();

        setRecentData(data1);
        console.log(data1);
      } catch (error) {
        console.log(error);
      }
    };

    fetchData();
    fetchStatus();
    fetchHeatingTemp();
    fetchRecentTemp();
  }, []);

  // turn OFF the heating system
  const handleOff = async () => {
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    };

    try {
      const res = await fetch(`${url}/turn_off_status`, options);
      const data = await res.json();

      console.log(data);
      setStatus(data.status);
    } catch (error) {
      console.log(error);
    }
  };

  // turn ON the heating system
  const handleOn = async () => {
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    };

    try {
      const res = await fetch(`${url}/turn_on_status`, options);
      const data = await res.json();

      console.log(data);
      setStatus(data.status);
    } catch (error) {
      console.log(error);
    }
  };

  // increment the value of the temperature
  const handlePLus = () => {
    setTemp(temp + 1);
  };

  // decrement the value of the temperature
  const handleMinus = () => {
    setTemp(temp - 1);
  };

  // set the final temperature
  const handleSet = async () => {
    console.log(temp);

    const value_temp = {
      value: temp,
    };

    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(value_temp),
    };

    try {
      const res = await fetch(
        `${url}/set_heating_temp`,
        options
      );
      const data = await res.json();

      console.log(data);
      setFinalTemp(data.temperature);
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
          </div>
          <div className="flex flex-col gap-8 sm:flex-row">
            <div className="w-full p-5 sm:w-2/4 flex flex-col items-center justify-center">
              <h1 className="mb-10 mt-10 text-3xl font-semibold">
                Home's data
              </h1>

              <div>
                <div className="bg-gray-900 h-40 w-40 flex justify-center items-center rounded-full mb-4 text-6xl border-4 border-white-300">
                  {recentData.temperature}
                  <sup className="text-lg">° C</sup>
                </div>
                <div className="bg-gray-900 h-40 w-40 flex justify-center items-center rounded-full text-6xl border-4 border-white-300">
                  {recentData.humidity}
                  <sup className="text-lg">%</sup>
                </div>
              </div>
            </div>
            <div className="w-full border-x-0 border-white-500 border-t-2 border-white-500 p-5 sm:w-2/4 sm:border-l-4 border-white-500 sm:border-t-0">
              <div>
                {status === 1 ? (
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
                  {status === 1 ? (
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
                  {temp} <sup className="text-lg"> ° C</sup>
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
