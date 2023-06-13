import mongoose from "mongoose";

const heatingStatusSchema = new mongoose.Schema({
    status:{
        type: Number,
        required: true,
        trim: true
    }
})

export default mongoose.model('HeatingStatus', heatingStatusSchema);