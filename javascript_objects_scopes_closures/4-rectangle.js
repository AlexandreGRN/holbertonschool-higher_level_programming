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

  // Exchange w/h
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Make the rectangle twice bigger
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
