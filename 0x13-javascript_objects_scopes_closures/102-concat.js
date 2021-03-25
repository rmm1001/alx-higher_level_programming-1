#!/usr/bin/node

const fs = require('fs');

const src1 = process.argv[2];
const src2 = process.argv[3];
const dest = process.argv[4];

try {
  const data1 = fs.readFile(src1);
  const data2 = fs.readFile(src2);
  fs.writeFile(dest, data1.toString() + data2.toString());
} catch (error) {
  console.error(`Got an error trying to read the file: ${error.message}`);
}
