#!/usr/bin/node

const arg1 = process.argv[2];

const x = Math.sqrt(arg1);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i <= x; i++) {
    console.log('X');
  }
}
