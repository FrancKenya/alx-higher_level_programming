#!/usr/bin/node

const request = require('request');

const apiUrl = `${process.argv[2]}?completed=true`;

function reqCallfunction (error, response, body) {
  if (!error) {
    const tasks = JSON.parse(body);
    const completed = {};
    tasks.forEach((task) => {
      if (task.completed && completed[task.userId] === undefined) {
        completed[task.userId] = 1;
      } else if (task.completed) {
        completed[task.userId] += 1;
      }
    });
    console.log(completed);
  }
}
request.get(apiUrl, reqCallfunction);
