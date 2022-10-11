#!/usr/bin/node

const toBeConverted = parseInt(process.argv[2]);
if (isNaN(toBeConverted)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + toBeConverted);
}
