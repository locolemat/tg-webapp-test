const express = require('express');
const app = express()
const path = require('path');
const fs = require('fs');
const https = require('https');

const options = {
    key: fs.readFileSync(path.join(__dirname, 'localhost-key.pem')),
    cert: fs.readFileSync(path.join(__dirname, 'localhost.pem')),
  };

PORT = process.env.PORT || 3500

app.get('^/$|/index.html', (req, res)=>{
    res.sendFile(path.join(__dirname, 'views', 'index.html'))
}) 

https.createServer(options, app).listen(PORT, ()=>{console.log(`Server listening on port ${PORT}`)});
