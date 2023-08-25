import { connectDB } from "./db.js";
import { PORT } from "./config.js";
import app from "./app.js";
import { Server } from "socket.io";
import http from "http"
import router from "./routes/posts_routes.js";
import HeatingStatus from "./models/HeatingStatus.js";
import HeatingTemp from "./models/HeatingTemp.js";

connectDB()

const server = http.createServer(app);

const io = new Server(server, {
    cors:{
        // origin: "https://smarthomeurluescu.go.ro/",
        // origin: "https://stalwart-eclair-182177.netlify.app",
        origin: "http://localhost:3000",
        methods: ["GET", "POST"]
    }
})


    io.on("connection", (socket) => {
        console.log("Conection socket");

        setInterval(async() => {

            const fetch_heating_status = async (req, res) => {
                try {    
                    const status = await HeatingStatus.find()
                    console.log(status);
                    socket.emit("serverMessage", status)   
                } catch (error) {
                    console.error(error);
                    return res.status(500).json({message: error.message})
                }
            }


            fetch_heating_status()
         
        }, 5000)

        setImmediate( async () => {
            
            const fetch_heating_temp = async (req, res) => {
                try {    
                    const heating_temp = await HeatingTemp.find()
                    console.log(heating_temp);
                    socket.emit("heating_temp_server", heating_temp)   
                    // res.send(heating_temp)
                    
                } catch (error) {
                    console.error(error);
                    return res.status(500).json({message: error.message})
                }
            }

            fetch_heating_temp()

        }, 15000)
    })


server.listen(PORT)
console.log(`Server is running port ${PORT}`);