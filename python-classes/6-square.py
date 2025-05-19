#!/usr/bin/python3
"""
Write class Square that defines a square by
Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):

Public instance method: def my_print(self): that prints in stdout
the square with the character #:
if size is equal to 0, print an empty line

Addition - position should be use by using space -
Don’t fill lines by spaces when position[1] > 0
"""


class Square:
    """
    A square class with Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer, otherwise raise a TypeError exception
    with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the
    message size must be >= 0

    Public instance method: def my_print(self):
    that prints in stdout the square with the character #:
    if size is equal to 0, print an empty line

    Addition - position should be use by using space -
    Don’t fill lines by spaces when position[1] > 0

    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size  # Triggers the setter (validation)
        self.position = position # Triggers the setter (validation)

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError ("position must be a tuple of 2 positive integers")
        self.__position = value
        

    def area(self):
        """
        Returns the current square area
        """

        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
            return
        
        # Print vertical offset
        for i in range(self.position[1]):
            print()

        for i in range(self.size):
            print(" " * self.position[0] + '#' * self.size)
    
