#!/usr/bin/node

const fs = require('fs');
const request = require('request');


const url = process.argv[2];
const fileName = process.argv[3];

request.get(url,
		(error, response, body) => {
    if (!error && response.statusCode === 200) {
        fs.writeFile(fileName, body, (err) => {
            if (err) throw err;
            console.log(`Webpage saved to ${fileName}`);
        });
    } else {
        console.log(`Error: ${error}`);
    }
});
