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

const url = process.env.REACT_APP_SERVER_URL;

const socket = io.connect(url, {
  transports: ["websocket"],
});

function App() {
  const [tempHome, setTempHome] = useState(0);
  const [humHome, setHumHome] = useState(0);
  const [statusHeating, setStatusHeating] = useState(0);
  const [treshold, setTreshold] = useState(0);
  const [isToggled, setIsToggled] = useState(false);
  const [showTresholdUpdateMessage, setShowTresholdUpdateMessage] =
    useState(false);

  useEffect(() => {
    try {
      socket.on("socket_status", (status) => {
        setStatusHeating(status);
      });
    } catch (error) {
      console.log(error);
    }
  }, []);

  useEffect(() => {
    try {
      socket.on("socket_temperature_And_Humidity", (data) => {
        setHumHome(data.humidity);
        setTempHome(data.temperature);
      });
    } catch (error) {
      console.log(error);
    }
  }, []);

  useEffect(() => {
    try {
      socket.on("socket_treshold", (data) => {
        setTreshold(data);
      });
    } catch (error) {
      console.log(error);
    }
  }, []);

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const res = await fetch(`${url}/status`);
        const data1 = await res.json();

        setStatusHeating(data1[0].status);
      } catch (error) {
        console.log(error);
      }
    };

    const fetchTreshold = async () => {
      try {
        const res = await fetch(`${url}/treshold`);
        const data = await res.json();

        setTreshold(data[0].temperature);
      } catch (error) {
        console.log(error);
      }
    };

    fetchStatus();
    fetchTreshold();
  }, []);

  useEffect(() => {
    const timer = setTimeout(async () => {
      setShowTresholdUpdateMessage(true);

      setTimeout(async () => {
        try {
          const temperature = treshold;

          const id = "64889e83c192652234604219";

          const data = await fetch(`${url}/update-treshold-from-web/${id}`, {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ temperature }),
          });

          const res = await data.json();

          if (res.message === "ok") {
            setShowTresholdUpdateMessage(false);
          }
        } catch (error) {
          console.log(error);
        }
      }, 3000);
    }, 5000);

    return () => {
      clearTimeout(timer);
    };
  }, [treshold]);

  useEffect(() => {
    if (statusHeating === 0) {
      setIsToggled(false);
    }

    if (statusHeating === 1) {
      setIsToggled(true);
    }
  }, [statusHeating]);

  const handlePLus = () => {
    const temperature = treshold + 0.5;
    setTreshold(temperature);
  };

  const handleMinus = () => {
    const temperature = treshold - 0.5;
    setTreshold(temperature);
  };

  const handleSlider = () => {
    setIsToggled(!isToggled);

    if (isToggled === false) {
      const statusOn = async () => {
        try {
          const status = 1;

          const id = "64889d6ce1b6713667bf6c89";

          const data = await fetch(`${url}/update-status/${id}`, {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ status }),
          });

          const res = await data.json();

          if (res.message === "On") {
            setStatusHeating(1);
          }
        } catch (error) {
          console.log(error);
        }
      };

      statusOn();
    }

    if (isToggled) {
      const statusOff = async () => {
        const status = 0;

        const id = "64889d6ce1b6713667bf6c89";

        try {
          const data = await fetch(`${url}/update-status/${id}`, {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ status }),
          });

          const res = await data.json();

          if (res.message === "Off") {
            setStatusHeating(0);
          }
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
          <Title title="Smart Heating" classStyle="text-6xl text-center" />
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
                  textStyle="text_temp_home"
                />
                <CircleData
                  data={humHome}
                  text="%"
                  classStyle="drop"
                  textStyle="text_hum_home"
                />
              </div>
            </div>
            <div className="w-full border-x-0 border-white-500 border-t-2 border-white-500 p-5 sm:w-2/4 sm:border-l-4 border-white-500 sm:border-t-0">
              <InfoMessage
                showTresholdUpdateMessage={showTresholdUpdateMessage}
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
                  heatingTemp={treshold}
                  classStyle1="drop_btn_treshold_active"
                  classStyle2="drop_btn_treshold"
                  text="° C"
                />

                <div className="flex flex-col h-full gap-20">
                  <CustomButton
                    functie={handlePLus}
                    classStyle="drop_btn"
                    text="+"
                    textStyle="text-7xl font-medium mt-2 ml-2"
                    disabled={isToggled}
                  />

                  <CustomButton
                    functie={handleMinus}
                    classStyle="drop_btn"
                    text="-"
                    textStyle="text-8xl font-medium mt-2 ml-2"
                    disabled={isToggled}
                  />
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
