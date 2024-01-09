#!/usr/bin/python3
''' module: 4-from_json_string
'''

import json


def from_json_string(my_str):
    ''' function: from_json_string
    accepts a JSON string and returns Python object
    '''
    return json.loads(my_str)
