#!/usr/bin/python3
""" sort a list """


class MyList(list):
    """ list class"""
    def print_sorted(self):
        """ print sorted """
        print(sorted(self))
