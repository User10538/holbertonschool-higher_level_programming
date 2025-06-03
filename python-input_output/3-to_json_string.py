#!/usr/bin/python3
"""
Write a function that returns the JSON
representation of an object (string):

"""


def to_json_string(my_obj):
    """
    Must use the with statement.

    Don’t need to manage file permission or file doesn't exist exceptions.
    """
    import json
    return json.dumps(my_obj)
