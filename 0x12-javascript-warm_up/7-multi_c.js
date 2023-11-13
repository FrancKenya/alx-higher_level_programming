#!/usr/bin/node
/*
 * Script that prints x times “C is fun”
 * x is the first argument of the script
 * If the first argument can’t be converted to an integer,
 * print “Missing number of occurrences”
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 * You can use only two console.log
 * You must use a loop (while, for, etc.)
 */

const x = parseInt(process.argv[2]);
if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
