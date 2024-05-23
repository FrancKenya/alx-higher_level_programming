#!/usr/bin/node

/* A module that reads a file, logs the output to stdout and outputs an error message if any */

const fs = require('fs');

// Gets file path from the command line arguments

const filePath = process.argv[2];

// Callback function to handle the file reading

function recall (err, data) {
	if (err) {
		console.error(err); // Use console.error for error messages
	} else {
	    console.log(data.toString()); // Print the file content to stdout
	}
}
// Read the file in utf-8 encoding
fs.readFile(filePath, 'utf8', recall);
