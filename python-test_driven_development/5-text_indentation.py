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

    skip_space = False
    for i in text:
        if skip_space and i == '':
            continue
            skip_space = False

        print("{}".format(i), end="")
        if i in {',', '?', ':'}:
            print("\n")
            skip_space = True
