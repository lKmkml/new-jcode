const express = require('express');
const path = require('path');

const app = express();

app.use(express.static(path.join(__dirname)));

app.listen(8000, function () {
  console.log('Video streaming server listening on port 8000!');
});
