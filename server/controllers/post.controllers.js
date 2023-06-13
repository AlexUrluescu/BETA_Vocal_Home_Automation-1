
import DataSenzors from "../models/DataSenzors.js";
import HeatingStatus from "../models/HeatingStatus.js";
import HeatingTemp from "../models/HeatingTemp.js";


export const getDataSenzors = async (req, res) => {
    try {    
        const data = await DataSenzors.find()
        res.send(data)
        
    } catch (error) {
        console.error(error);
        return res.status(500).json({message: error.message})
    }

};

export const getHeatingStatus = async (req, res) => {
    try {    
        const status = await HeatingStatus.find()
        res.send(status)
        
    } catch (error) {
        console.error(error);
        return res.status(500).json({message: error.message})
    }

};

export const getHeatingTemp = async (req, res) => {
    try {    
        const heating_temp = await HeatingTemp.find()
        res.send(heating_temp)
        
    } catch (error) {
        console.error(error);
        return res.status(500).json({message: error.message})
    }

};

export const changeStatus = async (req, res) => {

    try {
        const updateStatus = await HeatingStatus.findByIdAndUpdate(req.params.id, req.body, { new: true })
        console.log(updateStatus);
        return res.json({"message": "ok"});

    } catch (error) {
        return res.status(500).json({message: error.message})
        
    }
};   

export const changeHeatingTemp = async (req, res) => {

    try {
        const updateHeatingTemp = await HeatingTemp.findByIdAndUpdate(req.params.id, req.body, { new: true })
        console.log(updateHeatingTemp);
        return res.json({"message": "ok"});

    } catch (error) {
        return res.status(500).json({message: error.message})
        
    }
};   




