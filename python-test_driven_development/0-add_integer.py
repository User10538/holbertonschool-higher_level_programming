#!/usr/bin/python3
"""
This module is to add two integers.

The function adds a and b=98.

Returns:
Sum of the two integers of a and b

Raises:
TypeError: if a or b is nto a float or integer

"""


def add_integer(a, b=98):

    result = None
    result = int(a) + int(b)
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return result
