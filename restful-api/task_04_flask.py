#!/usr/bin/python3
import json
from flask import Flask, jsonify, request
app = Flask(__name__)

#users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
users = {}

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def data():
    usernames = list(users.keys())
    return jsonify(usernames), 200

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def GetUsers(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})

@app.route('/add_user', methods = ['POST'])
def AddUsers():
    #data = {"username": "john", "name": "John", "age": 30, "city": "New York"}
    data = request.get_json()

    username = data['username']

    users[username] = {"name": data.get("name", ""), 
                       "age": data.get("age", 0),
                       "city": data.get("city", "")}
    return jsonify(users[username])

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5000)
