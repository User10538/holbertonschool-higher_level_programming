#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        ### removes the item at the specified index ###
        del my_list[idx]
    return my_list
