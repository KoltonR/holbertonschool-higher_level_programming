#!/usr/bin/node

const process = require('process');
const args = process.argv;

function factorial (num) {
  num = parseInt(num);
  if (isNaN(num)) {
    return 1;
  }
  if (num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}

console.log(factorial(args[2]));
