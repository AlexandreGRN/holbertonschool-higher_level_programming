#!/usr/bin/python3
""" Creating square class """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialisation """
        super().__init__(height=size, width=size, x=x, y=y, id=id)

    # ---------- Size
    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        if value is None or type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.height = value
        self.width = value

    # ---------- Print and updating values
    def __str__(self):
        """ print the square infos """
        str = "[Square] ({}) {}/{} - {}"
        return str.format(self.id, self.x, self.y, self.height)
    
    def to_dictionary(self):
        """ return a newDict of all the variables """
        newDict = dict()
        try:
            newDict['x'] = self.x
        except:
            pass
        try:
            newDict['y'] = self.y
        except:
            pass
        try:
            newDict['id'] = self.id
        except:
            pass
        try:
            newDict['size'] = self.width
        except:
            pass
        return newDict

    def update(self, *args, **kwargs):
        """ Update the variables """
        if len(args) == 0:
            try:
                self.id = kwargs['id']
            except:
                pass
            try:
                self.width = kwargs['size']
            except:
                pass
            try:
                self.x = kwargs['x']
            except:
                pass
            try:
                self.y = kwargs['y']
            except:
                pass
        try:
            self.id = args[0]
        except:
            pass
        try:
            self.width = args[1]
        except:
            pass
        try:
            self.x = args[2]
        except:
            pass
        try:
            self.y = args[3]
        except:
            pass
