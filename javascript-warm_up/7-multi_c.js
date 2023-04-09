#!/usr/bin/node
/* Module */
const process = require('process');

/* Code */
// init
const argv = process.argv;
const c = 'C is fun';
let i = 0;
const max = Number(argv[2]);

// print
if (!max) {
  console.log('Missing number of occurrences');
} else {
  while (i < max) {
    console.log(c);
    i++;
  }
}
