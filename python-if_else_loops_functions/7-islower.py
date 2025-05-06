#!/usr/bin/python3

def islower(c):
    if isinstance(c, str) and len(c) ==1:
        return 'a' <= c <= 'z'
    return False
