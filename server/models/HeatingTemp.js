import mongoose from "mongoose";

const heatingTempSchema = new mongoose.Schema({
    temperature:{
        type: Number,
        required: true,
        trim: true
    }
})

export default mongoose.model('HeatingTemp', heatingTempSchema);