#!/usr/bin/python3

def islower(c):
    if len(c) != 1:
        raise ValueError("Input must be single char")
    if 'a' <= c <= 'z':
        return True
    else:
        return False
