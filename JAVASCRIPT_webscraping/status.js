#!/usr/bin/node

const req = require('request');
const API_URL = process.argv[2];

req.get(API_URL, function (error, response, body) {
	code = response.statusCode;
		console.log(`code: ${code}`)
//	}
});
