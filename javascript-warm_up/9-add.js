#!/usr/bin/node

const process = require('process');
const args = process.argv;

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  return a + b;
}

console.log(add(args[2], args[3]));
