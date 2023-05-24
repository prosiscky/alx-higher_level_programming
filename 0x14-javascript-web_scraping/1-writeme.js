#!/usr/bin/node
// a script that writes data to a file

// Import object fs into a variable fs
const fs = require('fs');

// create a variable file to hold file path
const file = process.argv[2];

// write to file
fs.writeFile(file, process.argv[3], { flag: 'w' }, (err) => {
  if (err) {
    console.log(err);
  }
});
