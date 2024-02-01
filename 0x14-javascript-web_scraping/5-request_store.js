#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

function fsCallfunction (err) {
  if (err) {
    console.log(err);
  }
}

function reqCallfunction (error, response, body) {
  if (!error) {
    fs.writeFile(filePath, body, 'utf-8', fsCallfunction);
  }
}
request.get(url, reqCallfunction);
