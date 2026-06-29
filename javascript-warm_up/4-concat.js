#!/usr/bin/node

const argumentUn = process.argv[2];
const argumentDeux = process.argv[3];

if (argumentUn && argumentDeux === undefined) {
  console.log('No argument');
} else { console.log(argumentUn + ' is ' + argumentDeux); }
