import { connectDB } from "./db.js";
import { PORT } from "./config.js";
import app from "./app.js";
import { Server } from "socket.io";
import http from "http"
import router from "./routes/posts_routes.js";
import HeatingStatus from "./models/HeatingStatus.js";

connectDB()

const server = http.createServer(app);

const io = new Server(server, {
    cors:{
        // origin: "https://smarthomeurluescu.go.ro/",
        origin: "https://stalwart-eclair-182177.netlify.app",
        // origin: "http://localhost:3000",
        methods: ["GET", "POST"]
    }
})


    io.on("connection", (socket) => {
        console.log("Conection socket");

        setInterval(async() => {

            const test = async (req, res) => {
                try {    
                    const status = await HeatingStatus.find()
                    console.log(status);
                    socket.emit("serverMessage", status)   
                } catch (error) {
                    console.error(error);
                    return res.status(500).json({message: error.message})
                }
            }

            test()
         
        }, 5000)
    })


server.listen(PORT)
console.log(`Server is running port ${PORT}`);