#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('update_header').addEventListener('click', function () {
    const header = document.querySelector('header');
    header.textContent = 'New Header!!!';
  });
});
