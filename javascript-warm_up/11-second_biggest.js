#!/usr/bin/node
/* Module */
const process = require('process');

/* Code */
// Init
const argv = process.argv;
let secondBiggest = 0;
let biggest = 0;
// Tests
if (argv.length <= 3) {
  console.log(0);
} else {
  // Check for second biggest
  argv.slice(2, argv.length).forEach((num) => {
    if (Number(num) > biggest) {
      secondBiggest = biggest;
      biggest = Number(num);
    }
  });
}
console.log(secondBiggest);
