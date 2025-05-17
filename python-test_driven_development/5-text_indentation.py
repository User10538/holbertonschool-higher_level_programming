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

    i = 0
    length = len(text)
    while i < length:
        line = ''
        while i < length and text[i] not in ".?:":
            line += text[i]
            i += 1

    print(line.strip())
    print()
    print()

    while i < length and text[i] == ' ':
        i += 1
        