import mongoose from "mongoose";

const dataSenzorsSchema = new mongoose.Schema({
    temperature:{
        type: Number,
        required: true,
        trim: true
    },
    humidity:{
        type: Number,
        required: true,
        trim: true
    },
    date:{
        type: Date,
        required: true,
        trim: true
    }
})

export default mongoose.model('DataSenzors', dataSenzorsSchema);