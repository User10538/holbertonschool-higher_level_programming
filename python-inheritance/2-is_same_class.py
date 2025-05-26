#!/usr/bin/python3
"""
Write a function that returns True if the
object is exactly an instance of the
specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Returns a True or False

    Args:
        obj: The object to inspect.
        a_class: the class

    Returns:
        Returns True if the object is exactly an instance
        of the specified class ; otherwise False
    """
    if not isinstance(obj, a_class):
        return "False"
    return "True"
