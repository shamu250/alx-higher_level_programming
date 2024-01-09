#!/usr/bin/python3
''' module: 3-to_json_string
'''

import json


def to_json_string(my_obj):
    ''' function: to_json_strin
    accepts an object and returns its JSON representation
    '''
    return json.dumps(my_obj)
