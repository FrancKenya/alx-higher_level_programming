#!/usr/bin/node

/* A script that displays the status code of a GET request */

const request = require('request');

// Gets the URL from the command line arguments
const url = process.argv[2];

function reqRecall (error, response, body) {
	if (!error) {
            console.log(`code: ${response.statusCode}`);
	}
}

request.get(process.argv[2], reqRecall);
