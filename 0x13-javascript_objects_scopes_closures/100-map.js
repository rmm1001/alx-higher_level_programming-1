#!/usr/bin/node
const list = require('./100-data');
const mapped = list.map(function (value, index) { return value * index; });
console.log(list);
console.log(mapped);
