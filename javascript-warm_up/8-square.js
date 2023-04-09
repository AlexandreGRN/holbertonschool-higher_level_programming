#!/usr/bin/node
/* Module */
const process = require('process');

/* Code */
// init
const argv = process.argv;
const character = 'X';
const size = Number(argv[2]);
let i = 0;
let j = 0;
let line = '';

// test size
if (!size) {
  console.log('Missing size');
} else {
// create line
  while (i < size) {
    line = line + character;
    i++;
  }

  // print created lines
  while (j < size) {
    console.log(line);
    j++;
  }
}
