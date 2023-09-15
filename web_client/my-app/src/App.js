import "./App.css";
import { useState, useEffect } from "react";
import {
  Title,
  CircleData,
  Slider,
  Treshold,
  CustomButton,
  InfoMessage,
  StatusHeating,
} from "./components";

import io from "socket.io-client";


// const url = "https://smarthome-dowt.onrender.com";
const url = "http://localhost:5000";

const socket = io.connect(url, {
  transports: ['websocket'],
});
// const socket = io.connect("http://localhost:5000");

socket.on("serverMessage", (data) => {
  console.log(data);
  // setStatusHeating(data[0])
});


function App() {
  // eslint-disable-next-line
  const [tempHome, setTempHome] = useState(23.0);
  const [humHome, setHumHome] = useState(89);
  const [statusHeating, setStatusHeating] = useState(0);
  const [heatingTemp, setHeatingTemp] = useState(0);

  const [isToggled, setIsToggled] = useState(false);
  // eslint-disable-next-line
  const [finalTemp, setFinalTemp] = useState();
  const [styleHeating, setStyleHeating] = useState(0);

  // useEffect(() => {
  //   const intervalId = setInterval(async () => {
  //     try {
  //       const res = await fetch(`${url}/senzor`);
  //       const data = await res.json();

  //       // setTempHome(data.temperature);
  //       // setHumHome(data.humidity);

  //       console.log(data);
  //     } catch (error) {
  //       console.log(error);
  //     }
  //   }, 5000);

  //   // Cleanup: oprește timer-ul când componenta se demontează
  //   return () => {
  //     clearInterval(intervalId);
  //   };
  // }, []);

  useEffect(() => {
    try {
      console.log("teeeeest");
      socket.on("serverMessage", (data) => {
        console.log(data);
        setStatusHeating(data)
      });

      console.log("teeeest iasa");

    } catch (error) {
      console.log(error);
    }

  }, [])

  // cod adaugat in idee_socket
  useEffect(() => {
    try {
      socket.on("heating_temp_server", (data) => {
        console.log(data);
        setHeatingTemp(data);
      })
      
    } catch (error) {
      console.log(error);
    }
  }, [])


  useEffect(() => {
    // get all the temperatures and humiditys
    // eslint-disable-next-line
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

        console.log(`status heating este: ${data1}`);
        setStatusHeating(data1[0].status);
        console.log(data1);
        console.log(data1[0].status);
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
        setHeatingTemp(data1[0].temperature);
        console.log(data1);
      } catch (error) {
        console.log(error);
      }
    };

    // fetchData();
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
          const temperature = heatingTemp;
          console.log(temperature);

          const id = "64889e83c192652234604219"

          const data = await fetch(
            `${url}/changeheatingtemp/${id}`,
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
            // send the socket
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
    if (statusHeating === 0) {
      setIsToggled(false);
    }

    if (statusHeating === 1) {
      setIsToggled(true);
    }
  }, [statusHeating]);

  // increment the value of the temperature
  const handlePLus = () => {
    // let temperature = heatingTemp.temperature;
    let temperature = heatingTemp + 0.5
    setHeatingTemp(temperature)
    // setHeatingTemp({ ...heatingTemp, temperature: temperature + 0.5 });
  };

  // decrement the value of the temperature
  const handleMinus = () => {
    // const temperature = heatingTemp.temperature;
    // setHeatingTemp({ ...heatingTemp, temperature: temperature - 0.5 });
    let temperature = heatingTemp - 0.5
    setHeatingTemp(temperature)
  };

  const handleVoid = () => {
    return "";
  };

  const handleSlider = () => {
    console.log(isToggled);
    setIsToggled(!isToggled);

    if (isToggled === false) {
      const statusOn = async () => {
        try {
          const status = 1;

          const id = "64889d6ce1b6713667bf6c89"

          const data = await fetch(`${url}/test/${id}`, {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ status }),
          });

          const res = await data.json();

          console.log(res);
          if (res.message === "On") {
            setStatusHeating(1);
          }
          // setStatus(data.status);
        } catch (error) {
          console.log(error);
        }
      };

      statusOn();
    }

    if (isToggled) {
      const statusOff = async () => {
        const status = 0;
        
        const id = "64889d6ce1b6713667bf6c89"

        try {
          const data = await fetch(`${url}/test/${id}`, {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ status }),
          });

          const res = await data.json();

          console.log(res);
          if (res.message === "Off") {
            setStatusHeating(0);
          }
          // setStatus(data.status);
        } catch (error) {
          console.log(error);
        }
      };

      statusOff();
    }
  };

  return (
    <div className="App">
      <div>
        <div className="p-3 w-screen">
          <Title title="Smart Heating" classStyle="text-6xl text-center"/>
          <div className="mt-8 flex flex-col gap-8 sm:flex-row">
            <div className="w-full p-5 sm:w-2/4 flex flex-col items-center justify-center">
              <Title
                title="Home's data"
                classStyle="text-3xl font-semibold mb-5"
              />
              <div className="flex flex-col items-center justify-center gap-10">
                <CircleData
                  data={tempHome}
                  text="° C"
                  classStyle="drop"
                  textStyle = "text_temp_home"
                />
                <CircleData
                  data={humHome}
                  text="%"
                  classStyle="drop"
                  textStyle = "text_hum_home"
                />
              </div>
            </div>
            <div className="w-full border-x-0 border-white-500 border-t-2 border-white-500 p-5 sm:w-2/4 sm:border-l-4 border-white-500 sm:border-t-0">
              <InfoMessage
                styleHeating={styleHeating}
                classStyle="h-10 mb-5 flex justify-center"
                textStyle="bg-green-500 text-white p-5 text-xl rounded-md w-90 flex justify-center items-center ease-in-out duration-300"
                text="Temperatura este actualizata"
              />
              <div className="text-center">
                <StatusHeating
                  isToggled={isToggled}
                  textStyle="text-2xl"
                  text1="On"
                  text2="Off"
                />
                <Slider
                  statusHeating={statusHeating}
                  rounded={true}
                  isToggled={isToggled}
                  onToggle={handleSlider}
                />
              </div>
              <div className="flex justify-center items-center gap-4 mt-10">
                <Treshold
                  isToggled={isToggled}
                  tempHome={tempHome}
                  heatingTemp={heatingTemp}
                  classStyle1="drop_btn_treshold_active"
                  classStyle2="drop_btn_treshold"
                  // classStyle1="bg-gray-900 h-40 w-40 flex justify-center items-center rounded-full text-6xl border-4 border-white-300"
                  text="° C"
                />

                {statusHeating === 1 ? (
                  <div className="flex flex-col h-full gap-20">
                    <CustomButton
                      functie={handlePLus}
                      classStyle="drop_btn"
                      text="+"
                      textStyle="text-7xl font-medium mt-2 ml-2"
                    />

                    <CustomButton
                      functie={handleMinus}
                      classStyle="drop_btn"
                      text="-"
                      textStyle="text-8xl font-medium mt-2 ml-2"
                    />
                  </div>
                ) : (
                  <div className="flex flex-col h-full gap-20">
                    <CustomButton
                      functie={handleVoid}
                      classStyle="drop_btn"
                      text="+"
                      textStyle="text-7xl font-medium mt-2 ml-2"
                    />

                    <CustomButton
                      functie={handleVoid}
                      classStyle="drop_btn"
                      text="-"
                      textStyle="text-8xl font-medium mt-2 ml-2"
                    />
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
