#!/usr/bin/python3
import pickle

def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    with open(filename, "wb") as f:
        pickle.dump(data, f)
    pass

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open(filename, "rb") as f:
        loaded_data = pickle.load(f)
        print(loaded_data)
    pass
