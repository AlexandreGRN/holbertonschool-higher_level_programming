#!/usr/bin/python3
""" create the triangle """


def pascal_triangle(n):
    """ create pascal trueiangle"""
    pascal = [[1]]
    for rowNumber in range(1, n):
        """ for each new row of numbers """
        row = []
        for numbersNumber in range(rowNumber + 1):
            if numbersNumber == 0 or numbersNumber == rowNumber:
                row.append(1)
            else:
                num1 = pascal[rowNumber-1][numbersNumber-1]
                num2 = pascal[rowNumber-1][numbersNumber]
                row.append(num1 + num2)
        pascal.append(row)
    return pascal
