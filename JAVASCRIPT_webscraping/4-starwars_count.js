#!/usr/bin/node

const req = require('request');
const url = process.argv[2];

req.get(url,
  function (err, res, body) {
    jsonBody = JSON.parse(body);
    results = jsonBody.results;
    let count = 0;
    results.forEach(function (movie, idx) {
      characters = movie.characters;
      characters.forEach(function (character, idx) {
        if (character.includes('18')) {
          count++;
        }
      });
    });
    console.log(count);
  });

/*  for (let i = 0; i++; i < results.length) {
  		characters = results[i].characters;
		for (let j = 0; j++; j < characters.length)) {
				if (characters[j].includes('18')) {
					count ++;
				}
		}
	}
*/







