#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text file
(UTF8) and returns the number of characters added:

"""


def append_write(filename="", text=""):
    """
    Must use the with statement.

    Don’t need to manage file permission or file doesn't exist exceptions.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
