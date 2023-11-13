#!/usr/bin/node

const argsCount = process.argv.length;

if ((argsCount - 2)  === 0) {
	console.log('No argument');
}
else if ((argsCount - 2) === 1) {
	console.log('Argument found');
}
else {
	console.log('Arguments found');
}
