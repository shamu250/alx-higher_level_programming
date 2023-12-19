#!/usr/bin/python3
import math


class MagicClass:
    ''' class: MagicClass  cuz it is'''

    def __init__(self, radius=0):
        ''' initialize MagicClass '''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        ''' calculate area of circle'''
        return self.__radius**2 * math.pi

    def circumference(self):
        '''calculate circumfrence of circle'''
        return 2 * math.pi * self.__radius
