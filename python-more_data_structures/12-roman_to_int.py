#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or roman_string == "":
        return 0
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    sum = 0
    prevValue = 0

    for i in reversed(roman_string):
        value = roman.get(i, 0)
        if value < prevValue:
            sum -= value
        else:
            sum += value
        prevValue = value
    return sum
