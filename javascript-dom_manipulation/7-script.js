#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const movies = data.results;
      const ul = document.getElementById('list_movies');

      movies.forEach(function (movies) {
        // to add li to ul
        const li = document.createElement('li');
        li.textContent = movies.title;
        ul.appendChild(li);
      });
    });
});
