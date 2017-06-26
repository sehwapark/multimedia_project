var express = require('express');
var app = express();
var request = require('request');
const fs = require('fs-extra');
var multer  = require('multer'),bodyParser = require('body-parser'),  path = require('path');
var PythonShell = require('python-shell');


app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/public'));
app.use(bodyParser.json());
//app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');
app.use(bodyParser({ uploadDir: __dirname + 'files' , keepExtensions: true }));


app.all('/', function(req,res){
    res.sendFile(__dirname + '/public/pages/index.html');
});
var jdata;
app.get('/result',function(req,res){
    res.send(jdata);
    res.end();
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
            var options = { mode : "text" , args : ["infer" , "--multi", "/none/sehwa/generated-embeddings/classifier.pkl" , new_location+file_name] };
            //PythonShell.run('../openface/demos/multimedia.py',options,function(err,results){
            PythonShell.run('../server.py',options,function(err,results){
                if(err) throw err;
                console.log(results);
                var _result;
                for(var i=0;i<results.length;i++){
                    _result = results[i];
                    if( _result.includes("{") ){
                        break;
                    }
                }

                jdata = JSON.parse(_result);
                var keys = Object.keys(jdata); 
                for ( var i = 0; i < keys.length;i++){
                    //console.log( jdata[keys[i]] );
                }
                //res.render('./public/pages/list.ejs',{array : jdata });
                res.sendFile(__dirname + '/public/pages/list.html');
            });
        }
    });
    //res.sendFile(__dirname + '/public/pages/list.html');
});
app.listen(8080,function(){
    console.log('Running Server...');
});
