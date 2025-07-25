#!/usr/bin/python3
import json
import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    response = requests.get(url)
    print("Status Code: 200")

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post['title'])
    else: 
        print(f"Status code print is missing or incorrect.")

def fetch_and_save_posts():
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Status Code: 200")
        data = response.json()

        filterPosts = []

        for post in data:
            filteredPosts = {'id': post['id'],
                          'title': post['title'],
                          'body': post['body']}
            filterPosts.append(filteredPosts)

        with open('posts.csv', "w", newline='', encoding="utf-8") as f:
            writeintoCSV = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writeintoCSV.writeheader()
            writeintoCSV.writerows(filterPosts)
