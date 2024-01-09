#!/usr/bin/python3
''' module: 8-base_geometry
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
    ''' Class: BaseGeometry
    inherits from BaseGeometry
    '''
    def __init__(self, width, height):
        '''method: __init__
        '''
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self._width = width
        self._height = height
