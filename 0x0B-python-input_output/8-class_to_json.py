#!/usr/bin/python3
'''module: 8-class_to_json
'''


def class_to_json(obj):
    '''class_to_json
    accepts: an object
    returns: builds a dictionary of attributes (no methods!) of the object
    '''
    return obj.__dict__
