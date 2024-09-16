const express = require("express");
const cookieParser = require("cookie-parser");
const path = require("path");
const app = express();
const port = 9090;
const host = '0.0.0.0';

app.use(cookieParser());

app.use(function (req, res, next) {
  // check if client sent cookie
  var cookie = req.cookies.username;
  if (cookie === undefined) {
    // no: set a new cookie
    res.cookie("username", "Z3Vlc3Q=", { maxAge: 900000, httpOnly: true });
    console.log("cookie created successfully");
  } else {
    // yes, cookie was already present
    console.log("cookie exists", cookie);
  }
  next(); // <-- important!
});

app.use(express.static("public"));

app.get("/", (req, res) => {
  const fileDirectory = path.resolve(__dirname, ".", "public/");
  res.sendFile("index.html", { root: fileDirectory });
});

app.get("/home", (req, res) => {
  const fileDirectory = path.resolve(__dirname, ".", "public/");
  res.sendFile("index.html", { root: fileDirectory });
});

app.get("/about", (req, res) => {
  const fileDirectory = path.resolve(__dirname, ".", "public/");
  res.sendFile("1.html", { root: fileDirectory });
});

app.get("/menu", (req, res) => {
  const fileDirectory = path.resolve(__dirname, ".", "public/");
  res.sendFile("1.html", { root: fileDirectory });
});

app.get("/secret", (req, res) => {
  const fileDirectory = path.resolve(__dirname, ".", "public/");
  if (req.cookies.username === "YWRtaW4=") {
    res.sendFile("secretwin.html", { root: fileDirectory });
  } else {
    res.sendFile("secretlose.html", { root: fileDirectory });
  }
});

app.listen(port, host, () => {
  console.log(`Example app listening on port ${port}`);
});
