#!/usr/bin/python3
# todo
# dict value | number
# test : if string null
# Return : number int
def roman_to_int(roman_string):
    number = 0
    numberList = []
    romanDict = {'I': 1,   'V': 5,
                 'X': 10,  'L': 50,
                 'C': 100, 'D': 500,
                 'M': 1000,
                }
    # test if string or not & null string
    if len(roman_string) == 0:
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
