#!/usr/bin/node
// A class "Rectangle" that defines a rectangle

// REQUIREMENTS
// - You must use the class notation for defining your class
// - The constructor must take 2 arguments: w and h
// - Initialize the instance attribute width with the value of w
// - Initialize the instance attribute height with the value of h
// - If w or h is equal to 0 or not a positive integer, create an empty object
// - Create an instance method called print() that prints the rectangle using the character X

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
}

module.exports = Rectangle;
