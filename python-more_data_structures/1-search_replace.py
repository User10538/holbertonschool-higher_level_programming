#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list =[]
    for i in my_list:
        if(i == search):
        #append is to add an item to the end of a list
            new_list.append(replace)
        else:
            new_list.append(i)
    return new_list
