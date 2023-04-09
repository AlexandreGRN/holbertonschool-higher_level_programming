#!/usr/bin/node
const Square5 = require('./5-square');
// Declaration of square
class Square extends Square5 {
  // Init
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let line = '';
    let customChara = 'X';
    if (c) {
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
