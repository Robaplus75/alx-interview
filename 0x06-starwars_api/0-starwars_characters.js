#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const k = JSON.parse(body).characters;
  exactOrder(k, 0);
});
const exactOrder = (k, num) => {
  if (num === k.length) return;
  request(k[num], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(k, num + 1);
  });
};
