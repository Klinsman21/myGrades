require('dotenv').config();

const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const corsOptions ={
  origin:'*', 
  credentials:true,            //access-control-allow-credentials:true
  optionSuccessStatus:200,
}


const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors(corsOptions));

const redis = require('./database/redis')
const mongodb = require('./database/mongo')


//app.get('/readSketch/:usrID', redis.ReadSketch);

app.post('/salvarAviso', (req, res) => {
  redis.salvarAviso(req.body.disciplina, req.body.aviso)
  res.end("ok");
})

app.get('/getLatLng/:matricula', mongodb.obterLocalizacao);

app.post('/salvarLocalizacao', (req, res) => {
  console.log(req.body.lat, req.body.lng)
  let obj = {
    'matricula': req.body.matricula,
    'lat': req.body.lat,
    'lng': req.body.lng
  }
  mongodb.salvarLocalizacao(obj)
  res.end("ok");
})

app.get('/deleteLocalizacao/:matricula', (req, res) => {
  console.log(req.params.matricula)
  mongodb.deleteLocalizacao(req.params.matricula)
  res.end("ok");
})


app.listen(process.env.PORT, () => { 
  console.log(`http://localhost:${process.env.PORT}`); 
});