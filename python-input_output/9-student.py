#!/usr/bin/python3
"""
Write a class Student that defines a student by:

Public instance attributes:
first_name
last_name
age

"""


class Student():
    """
    Instantiation with first_name, last_name and age:
    Public method def to_json(self): that retrieves a dictionary
    representation of a Student instance (same as 8-class_to_json.py)

    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
