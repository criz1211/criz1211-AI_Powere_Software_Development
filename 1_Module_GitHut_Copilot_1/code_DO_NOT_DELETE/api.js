// Create an Express.js server with a GET endpoint at /hello that returns "Hello, World!  "
const express = require('express');
const app = express();
const port = 3000;

app.get('/hello', (req, res) => {
    res.send('Hello, World!');
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});

// Add a POST endpoint at /data that accepts JSON and returns it      back
app.use(express.json());
app.post('/data', (req, res) => {
    res.json(req.body);
});
