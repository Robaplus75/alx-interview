#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const k = JSON.parse(body).characters;
  exactOrder(k, 0);
});

const exactOrder = (k, x) => {
  if (x === k.length) return;
  request(k[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(k, x + 1);
  });
};
