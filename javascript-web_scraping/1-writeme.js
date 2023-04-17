#!/usr/bin/node

// Module
const fs = require('fs');
const process = require('process');

// Open a new file with name input.txt and write Simply Easy Learning! to it.
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err) {
  if (err) throw err;
});
