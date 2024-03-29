const express = require('express');
const app = express()
const path = require('path');

PORT = process.env.PORT || 3500

app.get('^/$|/index.html', (req, res)=>{
    res.sendFile(path.join('views', 'index.html'))
}) 

app.listen(PORT, ()=>{console.log(`Server listening on port ${PORT}`)})