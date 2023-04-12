#!/usr/bin/node
// A function that executes x times a function
// The function must be visible from outside with prototype:
// function (x, theFunction)

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
