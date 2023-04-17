#!/usr/bin/node

// Module
const request = require('request');
const process = require('process');
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  fs.writeFile(process.argv[3], body, 'utf-8', function (err) {
    if (err) throw err;
  });
});
