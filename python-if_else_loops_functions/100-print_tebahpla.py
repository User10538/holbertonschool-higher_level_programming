#!/usr/bin/python3

def uppercase():
    result = ""
    for i in range(ord('z'), ord('a') -1, -1):
        if (ord('z') - i) % 2 == 0:
            result += "{}".format(chr(i).lowercase())
        else:
            result += "{}".format(chr(i).uppercase())

    print("{}".format(result))

    uppercase()
