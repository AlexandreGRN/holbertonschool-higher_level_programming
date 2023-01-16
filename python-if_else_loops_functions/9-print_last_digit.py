#!/usr/bin/python3
def print_last_digit(number):
    digt = abs(number) % 10
    print("{}".format(digt), end='')
    return(digt)
