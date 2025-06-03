#!/usr/bin/python3
"""
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

"""


def write_file(filename="", text=""):
    """
    Must use the with statement.

    Don’t need to manage file permission or file doesn't exist exceptions.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
