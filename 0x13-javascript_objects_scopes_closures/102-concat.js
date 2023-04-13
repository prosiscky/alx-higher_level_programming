#!/usr/bin/node
// A script that concats 2 files.

// REQUIREMENTS
// - The first argument is the file path of the first source file
// - The second argument is the file path of the second source file
// - The third argument is the file path of the destination

const fs = require('fs');

const fArg = fs.readFileSync(process.argv[2]).toString();
const sArg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fArg + sArg);
