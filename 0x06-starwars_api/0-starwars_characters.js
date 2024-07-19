#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const cURL = JSON.parse(body).characters;
    const cName = cURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, Body) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(Body).name);
        });
      }));

    Promise.all(cName)
      .then(names => console.log(names.join('\n')))
      .catch(Err => console.log(Err));
  });
}
