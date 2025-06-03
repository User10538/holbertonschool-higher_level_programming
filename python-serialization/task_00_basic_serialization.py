#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    with open(filename, "wb") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open(filename, "rb") as f:
        return json.load(f)
