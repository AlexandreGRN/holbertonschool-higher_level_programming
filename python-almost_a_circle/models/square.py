#!/usr/bin/python3
""" Creating square class """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    
    def __init__(self, size, x=0, y=0, id=None):
        """ initialisation """
        super().__init__(size, size, x, y, id)
        self.size = size
    
    @property
    def size(self):
        """ size getter """
        return self.__size

    def size(self, value):
        """ size setter """
        if value is None or type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__size = value

    def __str__(self):
        """ print the square infos """
        str = "[Square] ({}) {}/{} - {}"
        return str.format(self.id, self.x, self.y, self.size)
