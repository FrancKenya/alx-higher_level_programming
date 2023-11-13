#!/usr/bin/node

/*
 * script that prints the addition of 2 integers
 * first argument is the first integer
 * The second argument is the second integer
 * You have to define a function with this prototype: function add(a, b)
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 */

function add (a, b) {
	  return a + b;
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (!isNaN(arg1) && !isNaN(arg2)) {
	const result = add(arg1, arg2);
	console.log(result);
} else {
	  console.log('Invalid input. Please provide two integers.');
}
