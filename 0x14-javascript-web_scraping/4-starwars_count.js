#!/usr/bin/node

/* A script that prints the number of movies where the character "Wedge Antilles" is present */

const request = require('request');

function reqRecall (err, response, body) {
	if (!err) {
            const rslt = JSON.parse(body).rslt;
            console.log(rslt.reduce((count, movie) => {
                return movie.characters.find((character) => character.endsWith('/18/'))
                    ? count + 1
                    : count;
	    }, 0));
	}
}
request.get(process.argv[2], reqRecall);
