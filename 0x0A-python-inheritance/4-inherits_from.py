#!/usr/bin/python3
''' module: 4-inherits_from
'''


def inherits_from(obj, a_class):
    '''function inherits_from
    obj: an object
    a_class: a class
    returns True if type of obj inherits from a_class, but is not class
    '''
    return type(obj) != a_class and isinstance(obj, a_class)
