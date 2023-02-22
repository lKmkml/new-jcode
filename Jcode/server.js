const express = require('express');
const path = require('path');

const app = express();

app.use(express.static(path.join(__dirname)));

app.listen(5000, function () {
  console.log('Video streaming server listening on port 5000!');
});
