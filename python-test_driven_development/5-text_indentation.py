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

    result = ""

    for i in text:
        result += i

        if i in ".?:":
            print(result.strip())
            print()
            print()
            result = ""

    if result.strip():
        print(result.strip())
