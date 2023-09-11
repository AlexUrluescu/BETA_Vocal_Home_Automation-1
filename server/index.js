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
    origin: "http://localhost:3000",
    methods: ["GET", "POST"],
  },
});

io.on("connection", (socket) => {
  console.log("Conection socket");
});

router.put("/test/:id", async (req, res) => {
  try {
    const status = req.body.status;
    // console.log(status);

    const _id = req.params.id;
    // console.log(_id);

    if (status == 1) {
      try {
        const updateStatus = await HeatingStatus.findByIdAndUpdate(
          req.params.id,
          req.body,
          { new: true }
        );
        console.log(updateStatus);
        console.log("trimis status 1");
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
        console.log(updateStatus);
        console.log("trimis status 0");
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

router.put('/changeheatingtemp/:id', async (req, res) => {

  try {
      const updateHeatingTemp = await HeatingTemp.findByIdAndUpdate(req.params.id, req.body, { new: true })
      console.log(updateHeatingTemp.temperature);

      io.emit("heating_temp_server", updateHeatingTemp.temperature)

      return res.json({"message": "ok"});

  } catch (error) {
      return res.status(500).json({message: error.message})
      
  }
});


// io.on("connection", (socket) => {
//   console.log("Conection socket");

//   setInterval(async () => {
//     const fetch_heating_status = async (req, res) => {
//       try {
//         const status = await HeatingStatus.find();
//         console.log(status);
//         socket.emit("serverMessage", status);
//       } catch (error) {
//         console.error(error);
//         return res.status(500).json({ message: error.message });
//       }
//     };

//     fetch_heating_status();
//   }, 5000);

//   // setImmediate( async () => {

//   //     const fetch_heating_temp = async (req, res) => {
//   //         try {
//   //             const heating_temp = await HeatingTemp.find()
//   //             console.log(heating_temp);
//   //             socket.emit("heating_temp_server", heating_temp)
//   //             // res.send(heating_temp)

//   //         } catch (error) {
//   //             console.error(error);
//   //             return res.status(500).json({message: error.message})
//   //         }
//   //     }

//   //     fetch_heating_temp()

//   // }, 15000)
// });

server.listen(PORT);
console.log(`Server is running port ${PORT}`);
