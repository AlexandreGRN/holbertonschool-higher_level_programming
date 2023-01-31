#!/usr/bin/python3
""" This module is a first creation of empty class for a square """


class Square:

    """Empty class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialisation of the size, with some constraint"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position
        if size < 0 or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return the square area """
        return (self.__size)**2

    def my_print(self):
        """ Print a square of size size"""
        if (self.__size == 0):
            print()
        else:
            for space in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        self.__position = value

try:
    my_square = Square(3, "Position")
except Exception as e:
    print(e)