#!/usr/bin/python3
"""
Write a function that returns True if  if the object is an instance
of, or if the object is an instance of a class
that inherited from, the specified class, else False
"""


def is_kind_of_class(obj, a_class):
    """
    Returns a True or False

    Args:
        obj: The object to inspect.
        a_class: the class

    Returns:
        Returns True if the object is an instance
        of, or if the object is an instance of a class
        that inherited from, the specified class, else False
    """
    return type(obj) is a_class or isinstance(obj, a_class)
