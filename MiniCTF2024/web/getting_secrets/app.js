const express = require("express");
const path = require("path");
const app = express();
const port = 8080;
const host = '0.0.0.0';

app.use(express.static("public"));

app.get("/", (req, res) => {
  res.set("Misc-flag", "minictf{53cR37_h34D3r5_4r3n7_50_53cR37!}")
  const fileDirectory = path.resolve(__dirname, ".", "public/");
  res.sendFile("index.html", { root: fileDirectory });
});

app.get("/1", (req, res) => {
  res.set("Misc-flag", "minictf{53cR37_h34D3r5_4r3n7_50_53cR37!}")
  const fileDirectory = path.resolve(__dirname, ".", "public/");
  res.sendFile("index.html", { root: fileDirectory });
});

app.get("/2", (req, res) => {
  res.set("Misc-flag", "minictf{53cR37_h34D3r5_4r3n7_50_53cR37!}")
  const fileDirectory = path.resolve(__dirname, ".", "public/");
  res.sendFile("2.html", { root: fileDirectory });
});

app.get("/3", (req, res) => {
  res.set("Misc-flag", "minictf{53cR37_h34D3r5_4r3n7_50_53cR37!}")
  const fileDirectory = path.resolve(__dirname, ".", "public/");
  res.sendFile("3.html", { root: fileDirectory });
});

app.get("/4", (req, res) => {
  res.set("Misc-flag", "minictf{53cR37_h34D3r5_4r3n7_50_53cR37!}")
  const fileDirectory = path.resolve(__dirname, ".", "public/");
  res.sendFile("4.html", { root: fileDirectory });
});

app.get("/0", (req, res) => {
  res.set("Misc-flag", "minictf{53cR37_h34D3r5_4r3n7_50_53cR37!}")
  const fileDirectory = path.resolve(__dirname, ".", "public/");
  res.sendFile("0.html", { root: fileDirectory });
});

app.listen(port, host, () => {
  console.log(`Example app listening on port ${port}`);
});
