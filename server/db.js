import mongoose from "mongoose";
import {MONGODB_URI} from "./config.js";

const options = {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    socketTimeoutMS: 30000, // adaugăm opțiunea bufferTimeoutMS cu valoarea 3000 (3 secunde)
};

export async function connectDB(){
    try {
        await mongoose.connect(MONGODB_URI, options)
        console.log("Database is connected");
        
    } catch (error) {
        console.log(error);
        console.log("Database connection failed");
    }
}
