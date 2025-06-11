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
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
    # -- Usage example --
    # curl -X POST [URL] /
    #    -H "Content-Type: application/json" /
    #    -d '{"key1":"value1","key2":"value2"}'
def add_user():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error":"Username is required"}), 400
    if 'username' not in data:
        return jsonify({"error": "User not found"}), 201
    if username is users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5000)
