#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        # i multiples of 3 & 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        # i only multiples of 3
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz", end=' ')
        # i only multiples of 5
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz", end=' ')
        # i isn't neither a multiples of 3 nor 5
        else:
            print("{}".format(i), end=' ')
