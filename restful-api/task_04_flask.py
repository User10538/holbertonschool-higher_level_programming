#!/usr/bin/python3
import json, requests
from flask import Flask, jsonify
app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def data():
    return jsonify(users)

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def GetUsers(username):
    if username in users:
        return jsonify(users[username])
    else:
        return 'error: User not found'

@app.route('/add_user', methods = ['POST'])
def AddUsers():
    #data = {"username": "john", "name": "John", "age": 30, "city": "New York"}
    data = requests.get_json()

    username = data['username']

    users[username] = {"name": data.get("name", ""), 
                       "age": data.get("age", 0),
                       "city": data.get("city", "")}
    return jsonify(users[username])


    

if __name__ == "__main__": 
    app.run(port=8000)
