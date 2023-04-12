#!/usr/bin/node
// A function that increments and calls a function.
// Prototype: function (number, theFunction)

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
