#!/usr/bin/node

const { dict } = require('./101-data');

const reversedDict = {};
for (const [key, value] of Object.entries(dict)) {
  if (!reversedDict[value]) {
    reversedDict[value] = [Number(key)];
  } else {
    reversedDict[value].push(Number(key));
  }
}
console.log('New Dictionary:', reversedDict);
