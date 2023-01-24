#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    numberList = []
    romanDict = {'I': 1,   'V': 5,
                 'X': 10,  'L': 50,
                 'C': 100, 'D': 500,
                 'M': 1000}
    # test if string or not & null string
    if roman_string == ""
        return 0

    # convert string into list of int
    for romanCharacter in roman_string:
        for convertKey in romanDict:
            if romanCharacter == convertKey:
                numberList.append(romanDict[convertKey])

    # calculus - conversion list into int
    prevValue = 0
    for i in numberList:
        if (i > prevValue):
            number -= prevValue
        else:
            number += prevValue
        prevValue = i
    number += prevValue
    return number

    # "pincement de téton"
