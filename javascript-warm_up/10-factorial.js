#!/usr/bin/node
/* Module */
const process = require('process');

/* Code */
// Functions
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

// Init
const argv = process.argv;
const number = Number(argv[2]);

// Tests
if (!number) {
  console.log(1);
} else {
  console.log(factorial(number));
}
