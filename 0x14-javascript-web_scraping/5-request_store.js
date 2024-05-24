#!/usr/bin/node

/* A script that gets the contents of a webpage and stores it in a file */

const request = require('request');
const fs = require('fs');
const filename = process.argv[3];
const url = process.argv[2];

function fsRecall (err) {
  if (err) {
    console.log(err);
  }
}

function reqRecall (err, response, body) {
  if (!err) {
    fs.writeFile(filename, body, 'utf8', fsRecall);
  }
}

request.get(url, reqRecall);
