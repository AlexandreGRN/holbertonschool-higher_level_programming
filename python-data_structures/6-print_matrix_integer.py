#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for count, j in enumerate(i):
            if count != 0:
                print("", end=" ")
            print("{:d}".format(j), end="")
        print("")
