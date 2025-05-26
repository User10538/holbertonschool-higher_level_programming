#!/usr/bin/python3
"""
Write a function that returns the list of available

Args:
    obj: The object to inspect.

Returns:
        A list of strings representing the object's attributes and methods.
"""


def lookup(obj):
    return dir(obj)
