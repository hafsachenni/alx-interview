#!/usr/bin/node

const reqst = require('request');
const util = require('util');

const promise = util.promisify(reqst);

const getCharacter = async (url) => {
  const rspn = await promise(url);
  if (rspn.statusCode === 200) console.log(JSON.parse(rspn.body).name);
};

const getCharMovies = async (id) => {
  const url = `https://swapi.dev/api/films/${mvId}/`;
  const rspn = await promise(url);
  if (rspn.statusCode === 200) {
    const characters = JSON.parse(rspn.body).characters;
    for (const character of characters) {
      await getCharacter(character);
    }
  }
};

const mvId = process.argv[2];
getCharMovies(mvId);
