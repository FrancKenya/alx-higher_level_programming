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
  console.log(a + b);
}
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);
add(Number(arg1), Number(arg2));
