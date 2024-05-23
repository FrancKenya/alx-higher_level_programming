#!/usr/bin/node

/* A script that writes a string to a file. */

const fs = require('fs');

function recall (err, data) {
  if (err) {
    console.error(err); // Print the error object if an error occurs
  }
}
fs.writeFile(process.argv[2], process.argv[3], 'utf8', recall);
