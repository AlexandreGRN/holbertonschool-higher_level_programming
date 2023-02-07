#!/usr/bin/python3
def pascal_triangle(n):
    """ create pascal trueiangle"""
    pascal = [[1]]
    for rowNumber in range(1, n):
        """ for each new row of numbers """
        row = []
        for numbersNumber in range(rowNumber + 1):
            row.append("hello")
        pascal.append(row)
    return pascal
        
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(4))