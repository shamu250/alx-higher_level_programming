#!/usr/bin/python3
''' module: 10-square
'''


class BaseGeometry:
    ''' Class: BaseGeometry
    '''
    def area(self):
        ''' method: area
        raises exception
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''public method: integer_validator
        name: always a string
        value: positive integer
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    ''' Class: Rectangle
    inherits from BaseGeometry
    '''
    def __init__(self, width, height):
        '''method: __init__
        '''
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self._width = width
        self._height = height

    def area(self):
        '''method: area
        '''
        return self._width * self._height

    def __str__(self):
        '''method: __str__(self)
        '''
        return "[Rectangle] {}/{}".format(self._width, self._height)

    def print(self):
        '''methon: print(self)
        '''
        return __str__(self)


class Square(Rectangle):
    ''' Class: Square
    inherits from Rectangle
    '''

    def __init__(self, size):
        '''method: __init__
        '''
        BaseGeometry.integer_validator(self, "size", size)
        self._size = size
        self._width = size
        self._height = size

    def area(self):
        '''method: area
        '''
        return self._size ** 2
