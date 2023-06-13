import { Router } from "express"
import { getDataSenzors, getHeatingStatus, getHeatingTemp, changeStatus, changeHeatingTemp} from "../controllers/post.controllers.js";

const router = Router()

router.get('/datasenzors', getDataSenzors);
router.get('/heatingstatus', getHeatingStatus);
router.get('/heatingtemp', getHeatingTemp);

router.put('/changestatus/:id', changeStatus);
router.put('/changeheatingtemp/:id', changeHeatingTemp);


export default router