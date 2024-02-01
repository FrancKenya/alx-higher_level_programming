#!/usr/bin/node
/*
 * script that prints the title of a Star Wars movie where the episode
 * nnumber matches a given integer
 */

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node get-movie-title.js <movie-id>');
  process.exit(1);
}
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(`Title: ${movieData.title}`);
  } else {
    console.error('Error:', error || `Status Code: ${response.statusCode}`);
  }
});
