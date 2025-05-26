#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of
a class that inherited (directly or indirectly) from
the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Returns a True or False

    Args:
        obj: The object to inspect.
        a_class: the class

    Returns:
        Returns True if the object is an instance of
        a class that inherited (directly or indirectly) from
        the specified class ; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
