#!/usr/bin/node

// Module
const request = require('request');
const process = require('process');

// Function
let count = 0;
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  JSON.parse(body).results.forEach(element => {
    if (JSON.stringify(element).includes('people/18') === true) {
      count = count + 1;
    }
  });
  console.log(count);
});
