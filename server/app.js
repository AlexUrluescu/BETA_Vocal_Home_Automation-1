import express from "express";
import fileUpload from "express-fileupload";
import post_routes from "./routes/posts_routes.js";
import cors from "cors";

const app = express();

app.use(cors())

// middlewares
app.use(express.json());
app.use(fileUpload({
    useTempFiles: true,
    tempFileDir: './upload'
}))

// routes
app.use(post_routes);

export default app;