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
    You can assume json will always be a dictionary
    A dictionary key will be the public attribute name
    A dictionary value will be the value of the public attribute

    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key in json:
            self.__dict__[key] = json[key]
