#!/usr/bin/python3
"""
Write a function that returns the list of available
attributes and methods of an object:
Returns a list object
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the object's attributes and methods.
    """
    return dir(obj)
