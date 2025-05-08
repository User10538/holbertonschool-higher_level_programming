#!/usr/bin/python3

def uppercase():
    result = ""
    for i in range(ord('z'), ord('a') -1, -1):
        if 'a' <= chr(i) <= 'z':
            result += "{}".format(chr(i).upper())
        else:
            result += "{}".format(i)
    print("{}".format(result))

    uppercase()
