#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const translation = data.results;
      const ul = document.getElementById('hello');
      document.getElementById('hello').textContent = data.hello;
    });
});
