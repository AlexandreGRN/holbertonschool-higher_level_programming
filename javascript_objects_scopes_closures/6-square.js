#!/usr/bin/node
const Rectangle = require('./4-rectangle');
// Declaration of square
class Square extends Rectangle {
  // Init
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let line = '';
    if (!c) {
      customChara = 'X';
    } else {
      customChara = c;
    }
    for (let printj = 0; printj < this.width; printj++) {
      line = line + String(customChara);
    }
    for (let printi = 0; printi < this.height; printi++) {
      console.log(line);
    }
  }
}

module.exports = Square;
