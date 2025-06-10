#!/usr/bin/python3
import json
import requests

url = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts(self):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post['title'])

def fetch_and_save_posts(self):
    r = requests.get()
    r.json()
