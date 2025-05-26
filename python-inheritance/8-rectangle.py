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

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0: 
            raise ValueError(f"{name} must be greater than 0")

class Rectangle:
    """
    Write a class Rectangle that inherits from
    BaseGeometry (7-base_geometry.py).
    
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
