#!/usr/bin/python3
'''class for Rectangle'''

from models.base import Base


class Rectangle(Base):
    '''class for Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Intialize the Rectangle class'''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @classmethod
    def check_int(cls, class_property):
        '''set width'''
        if isinstance(class_property, int):
            class_property = class_property
        else:
            name_var = [key for key, value in locals().items() if value is class_property[0]]
            raise TypeError("{} must be an integer".format(name_var))

    @property
    def width(self):
        '''get width'''
        return self.__width

    @width.setter
    def width(self, width):
        '''set width'''
        if isinstance(width, int):
            self.__width = width
        else:
            raise TypeError("{} must be an integer".format(width))
        # Rectangle.check_int(width)

    @property
    def height(self):
        '''get height'''
        return self.__height

    @height.setter
    def height(self, height):
        '''set height'''
        Rectangle.check_int(height)

    @property
    def x(self):
        '''get x'''
        return self.__x

    @x.setter
    def x(self, x):
        '''set x'''
        Rectangle.check_int(x)

    @property
    def y(self):
        '''get y'''
        return self.__y

    @y.setter
    def y(self, y):
        '''set y'''
        Rectangle.check_int(y)
