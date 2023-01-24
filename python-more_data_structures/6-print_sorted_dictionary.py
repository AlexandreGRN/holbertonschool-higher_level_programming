#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # sort a dictionary
    sortedDict = dict(sorted(a_dictionary.items()))
    # print the full sorted dictionary
    for i in sortedDict:
        print("{}: {}".format(i, sortedDict[i]))
