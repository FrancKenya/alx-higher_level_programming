#!/usr/bin/node
/*
 * A script that computes and prints a factorial
 * The first argument is integer (argument can be cast as integer)
 * used for computing the factorial
 * Factorial of NaN is 1
 * You must do it recursively
 * You must use a function
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 */

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return (1);
  }
  if (n < 0) {
    return (-1);
  } else {
    return n * factorial(n - 1);
  }
}
const input = Number(process.argv[2]);
const result = factorial(input);
console.log(result);
