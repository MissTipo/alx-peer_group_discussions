#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(
			url,
			function(err, res, body) {
				todos = JSON.parse(body);
				output = {};
				todos.forEach(function (todo, idx) {
					if (todo.completed) {
			if (todo.userId in output) {
				output[todo.userId]++;
				} else {
					output[todo.userId] = 1
				}
					}
				});
				console.log(output);
});
