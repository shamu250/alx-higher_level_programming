#!/usr/bin/python3
''' module: 2-is_same_class
'''


def is_kind_of_class(obj, a_class):
    '''function: is_kind_of_class
    obj: an object
    a_class: a class
    returns True or False depending on if obj is instance of a_class,
    or is a subclass of a_class
    '''
    return isinstance(obj, a_class)
