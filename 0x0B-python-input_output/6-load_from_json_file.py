#!/usr/bin/python3
''' module: 6-load_from_json_file
'''

import json


def load_from_json_file(filename):
    '''function: load_from_json_file
    accepts: filename of file containing JSON string
    returns: corresponding Python object
    '''
    full_string = ""
    with open(filename, "r") as f:
        for line in f:
            full_string += line
    return json.loads(full_string)
