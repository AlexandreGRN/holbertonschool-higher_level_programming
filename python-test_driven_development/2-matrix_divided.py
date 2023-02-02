#!/usr/bin/python3
""" function divide all elem of a matrix """

def matrix_divided(matrix, div):
    """ (je deteste gab) """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    new_baby = []
    for row in matrix:
        new_baby = []
        for element in row:
            try:
                new_baby.append(round(element / div, 2))
            except:
                if not isinstance(element, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(new_baby) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append(new_baby)
    return(new_matrix)
