import { connectDB } from "./db.js";
import { PORT } from "./config.js";
import app from "./app.js";
import { Server } from "socket.io";
import http from "http";
import router from "./routes/posts_routes.js";
import HeatingStatus from "./models/HeatingStatus.js";
import HeatingTemp from "./models/HeatingTemp.js";

connectDB();

const server = http.createServer(app);

const io = new Server(server, {
  cors: {
    // origin: "https://smarthomeurluescu.go.ro/",
    // origin: "https://stalwart-eclair-182177.netlify.app",
    origin: "*",
    methods: ["GET", "POST", "PUT"],
  },
});

router.put("/test/:id", async (req, res) => {
  try {
    const status = req.body.status;

    const _id = req.params.id;

    if (status == 1) {
      try {
        const updateStatus = await HeatingStatus.findByIdAndUpdate(
          req.params.id,
          req.body,
          { new: true }
        );

        io.emit("serverMessage", 1);
        return res.json({ message: "On" });
      } catch (error) {
        console.log(error);
      }
    }
    if (status == 0) {
      try {
        const updateStatus = await HeatingStatus.findByIdAndUpdate(
          req.params.id,
          req.body,
          { new: true }
        );

        io.emit("serverMessage", 0);
        return res.json({ message: "Off" });
      } catch (error) {
        console.log(error);
      }
    }
  } catch (error) {
    return res.status(500).json({ message: error.message });
  }
});

// router.post("/datasenzor", (req, res) => {
//   const data = req.body;

//   io.emit("senzorTemperature", data.temperature);

//   const response = {
//     message: "Datele de la senzori au fost primite cu succes!",
//     body: data,
//   };

//   res.json(response);
// });

router.post("/sendSenzorTemperatureAndHumidity", (req, res) => {
  const data = req.body;

  io.emit("socket_temperature_And_Humidity", {
    humidity: data.humidity,
    temperature: data.temperature,
  });

  const response = {
    message: "Datele de la senzori au fost primite cu succes!",
    body: data,
  };

  res.json(response);
});

router.put("/update-treshold/:id", async (req, res) => {
  try {
    const updateTreshold = await HeatingTemp.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    );

    io.emit("socket_treshold", updateTreshold.temperature);

    return res.json({ message: "ok" });
  } catch (error) {
    return res.status(500).json({ message: error.message });
  }
});

router.put("/update-treshold-from-web/:id", async (req, res) => {
  try {
    const updateTreshold = await HeatingTemp.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    );

    if (updateTreshold) {
      return res.json({ message: "ok" });
    }
  } catch (error) {
    return res.status(500).json({ message: error.message });
  }
});

io.on("connection", (socket) => {
  console.log("a user connected" + socket.id);
});

server.listen(PORT);
console.log(`Server is running port ${PORT}`);
