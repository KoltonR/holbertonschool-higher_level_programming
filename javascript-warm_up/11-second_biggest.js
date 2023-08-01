#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  args.sort(function (a, b) {
    return a - b;
  });
  console.log(args[args.length - 2]);
}
