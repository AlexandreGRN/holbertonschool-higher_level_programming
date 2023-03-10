#!/usr/bin/python3
""" Creating rectangle Class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self, *args, **kwargs):
        """ Update the variables """
        if len(args) == 0:
            try:
                self.id = kwargs['id']
            except:
                pass
            try:
                self.width = kwargs['width']
            except:
                pass
            try:
                self.height = kwargs['height']
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
            self.height = args[2]
        except:
            pass
        try:
            self.x = args[3]
        except:
            pass
        try:
            self.y = args[4]
        except:
            pass

    # ---------- Width
    @property
    def width(self):
        """ get the width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width value to @width """
        if value is None or type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # ---------- Height
    @property
    def height(self):
        """ get the height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height value to @height """
        if value is None or type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # ---------- x
    @property
    def x(self):
        """ get the x value """
        return self.__x

    @x.setter
    def x(self, value):
        """ set the x value to @x """
        if value is None or type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # ---------- y
    @property
    def y(self):
        """ get the y value """
        return self.__y

    @y.setter
    def y(self, value):
        """ set the y value to @y """
        if value is None or type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # ---------- Area

    def area(self):
        """ return the area value of the rectangle """
        return self.width * self.height

    # ---------- Display
    def display(self):
        """ print the rectangle area including coordinate """
        for y in range(self.y):
            print("")
        for height in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for width in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """ print the rectangle infos """
        str = "[Rectangle] ({}) {}/{} - {}/{}"
        return str.format(self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """ return a dict of all the variables """
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
            newDict['height'] = self.height
        except:
            pass
        try:
            newDict['width'] = self.width
        except:
            pass
        return newDict
