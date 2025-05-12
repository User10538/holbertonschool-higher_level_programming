#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        new_in_list = my_list.copy()
        new_in_list[idx] = element
        return new_in_list
    return my_list.copy()
