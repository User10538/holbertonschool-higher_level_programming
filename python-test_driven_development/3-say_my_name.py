#!/usr/bin/python3

"""
This module is to prints My name is <first name> <last name>

"""

def say_my_name(first_name, last_name=""):
    """
    The function prints My name is <first name> <last name>:

    Returns:
    Prints My name is <first name> <last name>

    Raises:
    TypeError exception with the message first_name must be a string or last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("{} {}".format(first_name, last_name))
