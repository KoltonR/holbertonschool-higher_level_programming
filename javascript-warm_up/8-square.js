#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (!args[2] || isNaN(args[2])) {
  console.log('Missing size');
} else {
  for (let y = 0; y < parseInt(args[2]); y++) {
    for (let x = 0; x < parseInt(args[2]); x++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
