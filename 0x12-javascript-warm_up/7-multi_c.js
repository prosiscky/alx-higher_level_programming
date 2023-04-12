#!/usr/bin/node
// A script that prints “C is fun” x times.
// Where x is the first argument of the script
// If the first argument can’t be converted to an integer, print “Missing number of occurrences”
// You must use console.log(...) to print all output
// You are not allowed to use var
// You can use only two console.log
// You must use a loop (while, for, etc.)

const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  Number(x);
  for (let idx = 0; idx < x; idx++) {
    console.log('C is fun');
  }
}
