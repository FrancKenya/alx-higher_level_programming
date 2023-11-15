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
      console.log(''); // Handle width or height beingzero by printing an empty line
      return;
    }
    const row = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}
module.exports = Rectangle;
