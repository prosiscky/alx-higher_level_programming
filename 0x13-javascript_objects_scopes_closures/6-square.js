#!/usr/bin/node
// A class Square that defines a square and inherits from Square
//
// REQUIREMENTS
// - You must use the class notation for defining your class and extends
// - Create an instance method called charPrint(c) that prints the rectangle using the character c
// - If c is undefined, use the character X

const Squared = require('./5-square');
class Square extends Squared {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let lcv1 = 0; lcv1 < this.height; lcv1++) {
      let resu = '';
      for (let lcv2 = 0; lcv2 < this.width; lcv2++) {
        resu += c;
      }
      console.log(resu);
    }
  }
}

module.exports = Square;
