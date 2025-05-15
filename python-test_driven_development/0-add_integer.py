#!/usr/bin/python3
"""
This module is to add two integers.

"""


def add_integer(a, b=98):

    """
    The function adds a and b=98.

    Returns:
    Sum of the two integers of a and b

    Raises:
    TypeError: if a or b is nto a float or integer
    """

    result = None
    result = int(a) + int(b)
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    
    if a == float('inf') or a == float('-inf'):
        raise OverflowError("Cannot convert float to integer")
    if b == float('inf') or b == float('-inf'):
        raise OverflowError("Cannot convert float to integer")

    if isinstance(a, float) and a != a:
        raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float) and b != b:
        raise ValueError("cannot convert float NaN to integer")
    return result
