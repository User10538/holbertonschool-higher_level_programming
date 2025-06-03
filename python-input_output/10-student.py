#!/usr/bin/python3
"""
Write a class Student that defines a student by: (based on 9-student.py)

Public instance attributes:
first_name
last_name
age

"""


class Student():
    """
    Instantiation with first_name, last_name and age: 
    Public method  that retrieves a dictionary representation
    of a Student instance (same as 8-class_to_json.py):
    If attrs is a list of strings, only attribute names contained in this list must be retrieved.
    Otherwise, all attributes must be retrieved
    You are not allowed to import any module

    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        return self.__dict__
