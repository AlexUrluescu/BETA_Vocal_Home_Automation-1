import { Router } from "express"
import { getDataSenzors, getHeatingStatus, getHeatingTemp, changeHeatingTemp, testStatus, datasenzor, getSenzor} from "../controllers/post.controllers.js";

const router = Router()

router.get('/datasenzors', getDataSenzors);
router.get('/heatingstatus', getHeatingStatus);
router.get('/heatingtemp', getHeatingTemp);

// router.put('/changestatus/:id', changeStatus);
// router.put('/changeheatingtemp/:id', changeHeatingTemp);

// router.put('/test/:id', testStatus);

router.post('/datasenzor', datasenzor)
router.get('/senzor', getSenzor)

export default router