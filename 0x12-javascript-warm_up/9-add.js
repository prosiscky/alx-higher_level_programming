#!/usr/bin/node
// A script that prints the addition of 2 integers
// The first argument is the first integer
// The second argument is the second integer
// You have to define a function with this prototype: function add(a, b)

function add (a, b) {
  const result = a + b;
  console.log(result);
}
add(Number(process.argv[2]), Number(process.argv[3]));
