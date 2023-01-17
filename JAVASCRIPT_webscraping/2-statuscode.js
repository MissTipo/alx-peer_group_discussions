#!/usr/bin/node


const req = require('request');
const url = process.argv[2];

req.get(url,
		function (err, res, body) {
			code = res.statusCode;
			console.log(`code: ${code}`);
		}
);
