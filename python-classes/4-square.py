#!/usr/bin/python3
"""
Write class Square that defines a square by
Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
"""


class Square:
    """
    A square class with Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer, otherwise raise a TypeError exception
    with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the
    message size must be >= 0
    """

    def __init__(self, size=0):
        self.size = size  # Triggers the setter (validation)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area
        """

        return self.__size * self.__size
