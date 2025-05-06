#!/usr/bin/python3

def uppercase(str):
    result = ""
    for i in str:
        if 'a' <= i <= 'z':
            result += "{}".format(chr(ord(i) - 32))
        else:
            result += "{}".format(i)
    print("{}".format(result))
