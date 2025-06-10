#!/usr/bin/python3
import json
import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post['title'])
    else: 
        print(f"Failed to fetch post. Status code: {response.status_code}")

def fetch_and_save_posts():
    r = requests.get()
    r.json()
