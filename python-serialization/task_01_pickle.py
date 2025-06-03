#!/usr/bin/python3
import pickle

class CustomObject:

    def __init__(self, age, name, is_student):
        self.age = age


    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Student: {self.is_student}")
    
    def serialize(self, filename):
        with open(filename,"wb") as f:
            pickle.dump(self, f)
