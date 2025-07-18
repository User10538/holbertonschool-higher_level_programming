#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    with open(filename,"w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
