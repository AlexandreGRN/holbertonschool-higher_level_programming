#!/usr/bin/node

// Module
const request = require('request');
const process = require('process');

// Function
request(process.argv[2], function (error, response, body) {
    console.log('code: ', response && response.statusCode);
})
