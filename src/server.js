const express = require('express');

const port = process.env.PORT || 8000;

const app = express();

app.use(express.json());

app.get('*', (req, res) => {
    res.send('hello');
});

app.post('*', (req, res) => {
    console.log(req.body);

    res.send('post hello');
});

app.listen(port, () => {
    console.log('App is listening at port: ', port);
});
