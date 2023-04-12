#!/usr/bin/node
// Update the class Rectangle

// REQUIREMENTS
// - Create an instance method called rotate() that exchanges the width and the height of the rectangle
// - Create an instance method called double() that multiples the width and the height of the rectangle by 2

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let lcv1 = 0; lcv1 < this.height; lcv1++) {
      let resu = '';
      for (let lcv2 = 0; lcv2 < this.width; lcv2++) {
        resu += 'X';
      }
      console.log(resu);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
