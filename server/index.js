import { connectDB } from "./db.js";
import { PORT } from "./config.js";
import app from "./app.js";
import { Server } from "socket.io";
import http from "http"
import router from "./routes/posts_routes.js";
import HeatingStatus from "./models/HeatingStatus.js";

connectDB();

const server = http.createServer(app);

const io = new Server(server, {
    cors:{
        origin: "http://localhost:3000",
        methods: ["GET", "POST"]
    }
})


    io.on("connection", (socket) => {
        console.log("Conection socket");

        setInterval(async() => {
            try {
                const res = await fetch('https://smarthome-dowt.onrender.com/heatingstatus')
                const data = await res.json()
                console.log(data);
                socket.emit("serverMessage", data)

                
            } catch (error) {
                console.error(error);
                // return res.status(500).json({message: error.message})
            }
        }, 5000)
    })


server.listen(PORT)
console.log(`Server is running port ${PORT}`);