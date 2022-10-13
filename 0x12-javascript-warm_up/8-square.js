#!/usr/bin/node

const inputSize = parseInt(process.argv[2]);
let squareIndicator = '';

if (process.argv.length < 3 || isNaN(inputSize)) {
  squareIndicator = 'Missing size';
}
for (let i = 0; i < inputSize; i++) {
  for (let j = 0; j < inputSize; j++) {
    squareIndicator += 'X';
  }
  if (i !== inputSize - 1) {
    squareIndicator += '\n';
  }
}
console.log(squareIndicator);
