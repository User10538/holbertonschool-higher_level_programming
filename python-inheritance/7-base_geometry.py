#!/usr/bin/python3
"""
Write a class BaseGeometry (based on 6-base_geometry.py).
Raises an Exception with the message area() is not implemented
Raise a TypeError exception, with the message <name> must be an integer
Raise a ValueError exception with the message <name> must be greater than 0
"""


class BaseGeometry:
    """
    Write a class BaseGeometry (based on 6-base_geometry.py).
    Raises an Exception with the message area() is not implemented
    
    """
    def area(self):

        raise Exception("area() is not implemented")
    
    """
    Raise a TypeError exception, with the message <name> must be an integer
    Raise a ValueError exception with the message <name> must be greater than 0
    """
    def integer_validator(self, name, value):

        if value is not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0: 
            raise ValueError("<name> must be greater than 0")
