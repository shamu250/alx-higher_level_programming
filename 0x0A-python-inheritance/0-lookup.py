#!/bin/python3
''' module: 0-lookup
'''


def lookup(obj):
    ''' function: lookup()
    obj: an object
    returns a list of attribute of "obj"
    '''
    return dir(obj)
