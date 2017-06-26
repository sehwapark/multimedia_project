var express = require('express');
var app = express();
var request = require('request');
const fs = require('fs-extra');
var multer  = require('multer'),bodyParser = require('body-parser'),  path = require('path');
var PythonShell = require('python-shell');


app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/public'));
app.use(bodyParser.json());
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');
app.use(bodyParser({ uploadDir: __dirname + 'files' , keepExtensions: true }));


app.all('/', function(req,res){
    res.sendFile(__dirname + '/public/pages/index.html');
});
app.post('/project',multer({ dest: './files/'}).single('myfile'),function(req,res){
    var temp_path = req.file['path'];
    var file_name = req.file['originalname'];
    var new_location = "./files/"
    fs.move(temp_path, new_location + file_name, {  clobber : true }, function (err) {
        if (err) {
            console.error(err);
        } else {
            console.log(new_location + file_name + '  uploaded!');
            //options = { args : [new_location + file_name]};
            /*
            var shell = new PythonShell('./test.py', { mode: 'text '});
            shell.send('hello');
            shell.end(function (err,message) {
                if (err) throw err;
                console.log(message);
            });
            */
            var options = { mode : "text" , args : "hihi" };
            PythonShell.run('./test.py',options,function(err,results){
                if(err) throw err;
                console.log(results);
            });
        }
    });
    res.sendFile(__dirname + '/public/pages/list.html');
});
app.listen(8080,function(){
    console.log('Running Server...');
});
