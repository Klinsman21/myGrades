require('dotenv').config();

const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors());

const redis = require('./redis')
const mongo = require('./mongo')


app.get('/writeSketch/:usrID/text/:text', redis.WriteSketch);
app.get('/readSketch/:usrID', redis.ReadSketch);

app.get('/savePost/:usrID/body/:text/title/:title/date/:date', mongo.SavePost);
app.get('/readAllPosts/:usrID', mongo.getAllPosts);


app.post('/saveNeo4j', (req, res) => {
  const obj = {
    name: req.body.name,
    email: req.body.email,
  }
  neo4j.Create(obj)
  res.end("ok");
})

app.listen(process.env.PORT, () => { 
  console.log(`http://localhost:${process.env.PORT}`); 
});