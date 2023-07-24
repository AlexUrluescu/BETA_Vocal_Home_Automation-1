import express from "express";
import fileUpload from "express-fileupload";
import post_routes from "./routes/posts_routes.js";
import cors from "cors";

const app = express();

app.use(cors({
    origin: 'https://64be0762846f6e20a239588f--stalwart-eclair-182177.netlify.app'
  }))

// middlewares
app.use(express.json());
app.use(fileUpload({
    useTempFiles: true,
    tempFileDir: './upload'
}))

// routes
app.use(post_routes);

export default app;