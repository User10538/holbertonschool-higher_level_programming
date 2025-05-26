#!/usr/bin/python3
"""
Write a function that returns the list of available
attributes and methods of an object:
Returns a list object
"""


def lookup(obj):
    return dir(obj)
