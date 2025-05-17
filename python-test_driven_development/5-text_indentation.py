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

    special_chars = ['.', '?', ':']
    result = ''
    skip_space = False

    for char in text:
        if skip_space and char == ' ':
            continue  # Skip spaces right after punctuation
        skip_space = False

        result += char
        if char in special_chars:
            result += '\n\n'
            skip_space = True

    # Print each non-empty line without leading/trailing spaces
    for line in result.split('\n'):
        line = line.strip()
        if line:
            print(line)
