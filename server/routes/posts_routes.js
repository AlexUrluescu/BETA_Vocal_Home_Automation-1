import { Router } from "express";
import {
  getDataSenzors,
  getHeatingStatus,
  getHeatingTemp,
  getSenzor,
} from "../controllers/post.controllers.js";

const router = Router();

router.get("/datasenzors", getDataSenzors);
router.get("/heatingstatus", getHeatingStatus);
router.get("/heatingtemp", getHeatingTemp);
router.get("/senzor", getSenzor);

export default router;
