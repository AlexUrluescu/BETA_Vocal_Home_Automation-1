import "./App.css";
import { useState, useEffect } from "react";
import Slider from "./components/Slider";

const url = "https://smarthome-dowt.onrender.com";

function App() {
  // eslint-disable-next-line
  const [tempHome, setTempHome] = useState(0);
  const [humHome, setHumHome] = useState(0);
  const [statusHeating, setStatusHeating] = useState(0);
  const [heatingTemp, setHeatingTemp] = useState(0);

  const [isToggled, setIsToggled] = useState(false);
  // eslint-disable-next-line
  const [finalTemp, setFinalTemp] = useState();
  const [styleHeating, setStyleHeating] = useState(0);

  useEffect(() => {
    // get all the temperatures and humiditys
    const fetchData = async () => {
      try {
        const res = await fetch(`${url}/datasenzors`);
        const data1 = await res.json();

        setTempHome(data1[0].temperature);
        setHumHome(data1[0].humidity);
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

    fetchData();
    fetchStatus();
    fetchHeatingTemp();
  }, []);

  useEffect(() => {
    const timer = setTimeout(async () => {
      setFinalTemp(heatingTemp);

      console.log("salvat");
      console.log("inceput mesaj");
      setStyleHeating(1);

      setTimeout(async () => {
        try {
          const temperature = heatingTemp.temperature;

          const data = await fetch(
            `${url}/changeheatingtemp/${heatingTemp._id}`,
            {
              method: "PUT",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({ temperature }),
            }
          );

          const res = await data.json();

          console.log(res);
          if (res.message === "ok") {
            setFinalTemp({ ...heatingTemp, temperature: temperature });
          }
        } catch (error) {
          console.log(error);
        }
        console.log("sfarsit mesaj");
        setStyleHeating(0);
      }, 3000);

      console.log("iasa");
    }, 5000);

    return () => {
      console.log("intra");
      clearTimeout(timer);
    };
  }, [heatingTemp]);

  useEffect(() => {
    console.log(isToggled);

    const statusOn = async () => {
      const status = 1;

      try {
        // de trecut url adevarat, inloc de localhost
        const data = await fetch(`http://localhost:5000/test/${status}`);

        const res = await data.json();

        console.log(res);
        if (res.message === "ok") {
          setStatusHeating({ ...statusHeating, status: 1 });
        }
        // setStatus(data.status);
      } catch (error) {
        console.log(error);
      }
    };

    const statusOff = async () => {
      const status = 0;

      try {
        const data = await fetch(`http://localhost:5000/test/${status}`);

        const res = await data.json();

        console.log(res);
        if (res.message === "ok") {
          setStatusHeating({ ...statusHeating, status: 0 });
        }
        // setStatus(data.status);
      } catch (error) {
        console.log(error);
      }
    };

    if (isToggled) {
      statusOn();
    } else {
      statusOff();
    }
  }, [isToggled, statusHeating]);

  // turn OFF the heating system
  // const handleOff = async () => {
  //   const status = 0;

  //   try {
  //     const data = await fetch(`${url}/changestatus/${statusHeating._id}`, {
  //       method: "PUT",
  //       headers: {
  //         "Content-Type": "application/json",
  //       },
  //       body: JSON.stringify({ status }),
  //     });

  //     const res = await data.json();

  //     console.log(res);
  //     if (res.message === "ok") {
  //       setStatusHeating({ ...statusHeating, status: 0 });
  //     }
  //     // setStatus(data.status);
  //   } catch (error) {
  //     console.log(error);
  //   }
  // };

  // turn ON the heating system
  // const handleOn = async () => {
  //   const status = 1;

  //   try {
  //     const data = await fetch(`${url}/changestatus/${statusHeating._id}`, {
  //       method: "PUT",
  //       headers: {
  //         "Content-Type": "application/json",
  //       },
  //       body: JSON.stringify({ status }),
  //     });

  //     const res = await data.json();

  //     console.log(res);
  //     if (res.message === "ok") {
  //       setStatusHeating({ ...statusHeating, status: 1 });
  //     }
  //     // setStatus(data.status);
  //   } catch (error) {
  //     console.log(error);
  //   }
  // };

  // increment the value of the temperature
  const handlePLus = () => {
    const temperature = heatingTemp.temperature;
    setHeatingTemp({ ...heatingTemp, temperature: temperature + 1 });
  };

  // decrement the value of the temperature
  const handleMinus = () => {
    const temperature = heatingTemp.temperature;
    setHeatingTemp({ ...heatingTemp, temperature: temperature - 1 });
  };

  // set the final temperature
  // const handleSet = async () => {
  //   const temperature = heatingTemp.temperature;

  //   try {
  //     const data = await fetch(`${url}/changeheatingtemp/${heatingTemp._id}`, {
  //       method: "PUT",
  //       headers: {
  //         "Content-Type": "application/json",
  //       },
  //       body: JSON.stringify({ temperature }),
  //     });

  //     const res = await data.json();

  //     console.log(res);
  //     if (res.message === "ok") {
  //       setHeatingTemp({ ...heatingTemp, temperature: temperature });
  //     }
  //   } catch (error) {
  //     console.log(error);
  //   }
  // };

  const handleSlider = () => {
    setIsToggled(!isToggled);
  };

  return (
    <div className="App">
      <div className="bg-slate-700 text-white flex justify-center items-center p-10 pb-20 sm:h-screen">
        <div className="p-3 w-screen">
          <div className="p-3 mb-20">
            <h1 className="text-6xl font-semibold">Smart Heating</h1>
          </div>
          <div className="flex flex-col gap-8 sm:flex-row">
            <div className="w-full p-5 sm:w-2/4 flex flex-col items-center justify-center">
              <h1 className="mb-20 text-3xl font-semibold">Home's data</h1>
              <div className="flex flex-col items-center justify-center gap-10">
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
              <div className="h-10 mb-5 flex justify-center">
                {styleHeating === 1 ? (
                  <p className="bg-green-500 text-xl rounded-md w-72 flex justify-center items-center ease-in-out duration-300">
                    Temperatura este actualizata
                  </p>
                ) : (
                  <p> </p>
                )}
              </div>
              <div>
                <div>
                  {isToggled === true ? (
                    <h2 className="text-2xl">On</h2>
                  ) : (
                    <h2 className="text-2xl">Off</h2>
                  )}
                </div>
                <Slider
                  rounded={true}
                  isToggled={isToggled}
                  onToggle={handleSlider}
                />
              </div>
              <div className="flex justify-center items-center gap-4">
                <div>
                  <div
                    className={
                      isToggled === true && tempHome < heatingTemp.temperature
                        ? "bg-gray-900 h-40 w-40 flex justify-center items-center rounded-full text-6xl border-8 border-yellow-300"
                        : "bg-gray-900 h-40 w-40 flex justify-center items-center rounded-full text-6xl border-4 border-white-300"
                    }
                  >
                    {heatingTemp.temperature}{" "}
                    <sup className="text-lg"> ° C</sup>
                  </div>
                </div>

                {statusHeating.status === 1 ? (
                  <div className="flex flex-col h-full gap-20">
                    <button onClick={handlePLus} className="btn">
                      +
                    </button>
                    <button onClick={handleMinus} className="btn">
                      -
                    </button>
                  </div>
                ) : (
                  <div className="flex flex-col h-full gap-20">
                    <button className="btn">+</button>
                    <button className="btn">-</button>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
