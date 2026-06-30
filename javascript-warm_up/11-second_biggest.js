#!/usr/bin/node

const number = process.argv.slice(2);

if (number.length < 2) {
  console.log(0);
} else {
  const num = number.map(Number).sort((a, b) => b - a);

  console.log(num[1]);
}
