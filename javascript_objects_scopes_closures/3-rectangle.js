#!/usr/bin/node
// Declaration Of the class
class Rectangle {
  // Init
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Print the Rectangle
  print () {
    let line = '';
    for (let printj = 0; printj < this.width; printj++) {
      line = line + 'X';
    }
    for (let printi = 0; printi < this.height; printi++) {
      console.log(line);
    }
  }
}

module.exports = Rectangle;
