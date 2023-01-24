#!/usr/bin/python3
def uniq_add(my_list=[]):
    # set() supress every multiples elems by transforming an array into a set
    sets = set(my_list)

    # sum every elem
    return sum(sets)
