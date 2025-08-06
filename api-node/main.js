const express = require('express');
const app = express();
const port = 5000;
var fs = require('fs');

app.use(express.json());

app.get('/check', (req, res) => {
    res.status(200).send('OK');
})

app.get('/info', function(req, res){
    fs.readFile(__dirname + '/' + 'info2.json', 'utf8', function(err, data){
        console.log(data);
        res.end(data);
    })
})

var server = app.listen(port, function() {
    var host = server.address().address;
    var port = server.address().port;
    console.log("API Node listening at http://%s:%s", host, port);
})