#!/usr/bin/node
let process = require('process')
let args = process.argv.slice(2)
let request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + args[0], function(err, res, body){
  console.log(JSON.parse(body).title)
});
