#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if bool(my_list) == 0:
        return "False"
    else:
        return "True"
    
    for i in my_list:
        if i != '2':
            return i
    result = []
    for i in my_list:
        result.append(i % 2 == 0)
        return result
