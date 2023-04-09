#!/usr/bin/node
// Module
const process = require('process');

// Code
const argv = process.argv;
if (argv.length > 2) {
  console.log(argv[2]);
}
