#!/usr/bin/python3
"""
Write a class MyList that inherits from list:
Prints the list, but sorted (ascending sort)
all the elements of the list will be of type int
"""


class MyList:
    """
    print out the list in ascending order
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
