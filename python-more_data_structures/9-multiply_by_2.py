#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for i in a_dictionary:
        new_value = a_dictionary[i] * 2
        new_dictionary[i] = new_value
    return new_dictionary
