#!/usr/bin/node
// A function that returns the reversed version of a list

// REQUIREMENTS
// - Prototype: exports.esrever = function (list)
// - You are not allow to use the built-in method reverse

exports.esrever = function (list) {
  let lent = list.length - 1;
  let i = 0;
  while ((lent - i) > 0) {
    const tmp = list[lent];
    list[lent] = list[i];
    list[i] = tmp;
    i++;
    lent--;
  }
  return list;
};
