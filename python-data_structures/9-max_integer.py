#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    largest_int = my_list[0]
    for num in my_list:
        if largest_int < num:
            largest_int = num
    return largest_int
