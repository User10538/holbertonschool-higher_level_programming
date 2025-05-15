#!/usr/bin/python3

"""
This module is to prints My name is <first name> <last name>.

"""


def print_square(size):
    """
    The function prints a square with the character #:

    Returns:
    Prints a square with the character #

    Raises:
    TypeError exception with the message size must be an integer. 
    ValueError exception with the message size must be >= 0.
    TypeError exception with the message size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and (size < 0):
        raise TypeError("size must be an integer") 

    for i in range(size):
        print("#" * size)
