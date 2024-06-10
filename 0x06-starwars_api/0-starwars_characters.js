#!/usr/bin/node
/**
 * Displays all the characters from a Star Wars movie
 */

const request = require('request');
const movieID = process.argv[2] + '/';
const movieAPI = 'https://swapi-api.hbtn.io/api/films/';
// Initiates API request, allowing for awaiting promises
request(movieAPI + movieID, async (error, response, body) => {
  if (error) return console.error(error);

  // Retrieves URLs of each character in the film
  const characterURLs = JSON.parse(body).characters;

  // Utilizes the URL list to fetch character details
  // Awaiting ensures orderly resolution of requests
  for (const characterURL of characterURLs) {
    await new Promise((resolve, reject) => {
      request(characterURL, (error, response, body) => {
        if (error) return console.error(error);

        // Retrieves and prints each character's name in the order of their URLs
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
