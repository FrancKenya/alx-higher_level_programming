#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (!this.width || !this.height) {
      console.log(''); // If width or height is missing or zero, print an empty line
      return;
    }
    const row = 'X'.repeat(this.width); // Create a row of X characters with width
    for (let i = 0; i < this.height; i++) {
      console.log(row); // Print the row 'height' times to form a rectangle
    }
  }
}
module.exports = Rectangle;
