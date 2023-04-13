#!/usr/bin/node
// A script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

// REQUIREMENTS
// - Your script must import dict from the file 101-data.js
// - In the new dictionary:
// - A key is a number of occurrences
// - A value is the list of user ids
// - Print the new dictionary at the end

const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const j in valsUniq) {
  const list = [];
  for (const k in totalist) {
    if (totalist[k][1] === valsUniq[j]) {
      list.unshift(totalist[k][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}
console.log(newDict);
