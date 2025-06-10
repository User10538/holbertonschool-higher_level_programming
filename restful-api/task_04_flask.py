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
    return jsonify({"OK"}), 200

@app.route('/users/<username>')
def GetUsers(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods = ['POST'])
def AddUsers():
    #data = {"username": "john", "name": "John", "age": 30, "city": "New York"}
    data = request.get_json()

    username = data.get("username")

    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    if not username:
        return jsonify({"error": "Missing username"}), 400
    
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    try:
        age = int(data.get("age", 0))
    except (ValueError, TypeError):
        age = 0

    users[username] = {"username" : username,
                       "name": data.get("name", ""), 
                       "age": data.get("age", age),
                       "city": data.get("city", "")}
    
    print("Returning user data:", users[username]) 

    return jsonify(users[username]), 200

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5000)
