#!/usr/bin/python3
import pickle

class CustomObject:

    def __init__(self, age, name, is_student):
        self.age = age
        self.name = name
        self.is_student = is_student


    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Student: {self.is_student}")
    
    def serialize(self, filename):
        with open(filename,"wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except(pickle.PickleError):
            print("File is corrupted.")
        return
