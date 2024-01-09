#!/usr/bin/python3
''' module: 2-is_same_class
'''


def is_same_class(obj, a_class):
    '''function: is_same_class
    obj: an object
    a_class: a class
    returns True or False depending on if obj is of type a)class,
    and not a subclass of a_class
    '''
    return type(obj) == a_class
