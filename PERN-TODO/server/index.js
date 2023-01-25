const express = require("express");
const app = express();
const cors = require("cros");

//middleware 
app.use(cors());
app.use(express.json());

app.listen(3005, () => {
  console.log("server has started on port 3005");
});