#!/usr/bin/node
const Rectangle = require('./4-rectangle');
// Declaration of square
class Square extends Rectangle {
  // Init
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
