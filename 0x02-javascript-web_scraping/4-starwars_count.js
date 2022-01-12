#!/usr/bin/node
const request = require('request');
const GET = request.get;
const url = process.argv[2];

GET(url, (err, res, body) => {
  if (err) return (console.log(err));
  const movies(filename, body, 'utf8', (err) => {
    if (err) return (console.log(err));
  });
]);
