#!/usr/bin/node

/*
 * A script that searches the second biggest integer in the list of arguments
 * all arguments can be converted to integer
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 */

const args = process.argv.slice(2).map(arg => Number(arg));

if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
