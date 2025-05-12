#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a_first_element = tuple_a[0] if len(tuple_a) > 0 else 0
    a_second_element = tuple_a[1] if len(tuple_a) > 1 else 0

    b_first_element = tuple_b[0] if len(tuple_b) > 0 else 0
    b_second_element = tuple_b[1] if len(tuple_b) > 1 else 0

    return a_first_element + a_second_element , b_first_element + b_second_element
