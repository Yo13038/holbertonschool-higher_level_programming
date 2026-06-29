#!/usr/bin/node

function factorial (x) {
  if (Number.isNaN(x) || x <= 1) {
    return 1;
  }
  return x * factorial(x - 1);
}

const number = parseInt(process.argv[2], 10);

console.log(factorial(number));
