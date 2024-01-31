#!/usr/bin/node

/*
 * A script that writes a string to a file
 */

const fs = require('fs');

function callback (err, data) {
  if (err) {
    console.log(err);
  }
}
fs.writeFile(process.argv[2], process.argv[3], 'utf8', callback);
