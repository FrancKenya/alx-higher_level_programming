#!/usr/bin/node

/*
 * A script that display the status code of a GET request.
 */

const request = require('request');

function reqCallback (error, response, body) {
  if (!error) {
    console.log(`code: ${response.statusCode}`);
  }
}
request.get(process.argv[2], reqCallback);
