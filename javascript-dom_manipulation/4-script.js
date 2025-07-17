#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('add_item').addEventListener('click', function () {
    const list = document.querySelector('.my_list'); // use class instead of id
    const newList = document.createElement('li');
    newList.textContent = 'Item';

    list.appendChild(newList);
  });
});
