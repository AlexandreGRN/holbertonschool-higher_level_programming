#!/usr/bin/node

// Module
const request = require('request');
const process = require('process');

// Function
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (error, response, body) {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
