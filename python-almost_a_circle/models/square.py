#!/usr/bin/python3
""" Creating square class """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialisation """
        super().__init__(height=size, width=size, x=x, y=y, id=id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        if value is None or type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.height = value
        self.width = value

    def __str__(self):
        """ print the square infos """
        str = "[Square] ({}) {}/{} - {}"
        return str.format(self.id, self.x, self.y, self.height)
