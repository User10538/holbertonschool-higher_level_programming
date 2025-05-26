#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle (9-rectangle.py):

size must be a positive integer, validated by integer_validator
the area() method must be implemented
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """
    Write a class Square that inherits from Rectangle (9-rectangle.py):

    """
    def __init__(self, size):
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2 # Area = side × side

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
