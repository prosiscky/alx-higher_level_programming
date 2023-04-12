#!/usr/bin/node
// A script that searches for the second biggest integer in the list of arguments
// assume all arguments can be converted to integer
// If no argument is passed, print 0
// If the number of arguments is 1, print 0

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).map(Number);
  const second = arr.sort(function (a, b) { return b - a; })[1];
  console.log(second);
}
