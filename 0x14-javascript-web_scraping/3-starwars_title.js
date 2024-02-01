#!/usr/bin/node
/*
 * script that prints the title of a Star Wars movie where the episode
 * nnumber matches a given integer
 */

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (!error) {
    const movieData = JSON.parse(body).title;
    console.log(movieData);
  }
});
