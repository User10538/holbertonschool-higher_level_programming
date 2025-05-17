#!/usr/bin/python3

"""
This module is to prints a text with 2 new lines
after each of these characters: ., ? and :

"""


def text_indentation(text):
    """
    The function prints a text with 2 new lines after
    each of these characters: ., ? and :

    Returns:
    Prints a text with 2 new lines after each of
    these characters: ., ? and :

    Raises:
    TypeError exception with the message text must be a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    for i, c in enumerate(text):
        if c in ".?:":
            print(text[start:i + 1].strip())
            start = i + 1
            while start < len(text) and text[start] == ' ':
                start += 1
    if start < len(text):
        print(text[start:].strip())
