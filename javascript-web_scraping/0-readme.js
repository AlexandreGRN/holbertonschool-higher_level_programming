#!/usr/bin/node

// Module
const fs = require('fs');
const process = require('process');

// Function
fs.readFile(process.argv[2], 'utf-8', (err, read) => {
    if (err) throw err;
    console.log(read.toString());
})
