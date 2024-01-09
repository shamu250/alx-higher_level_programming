#!/usr/bin/python3
''' module: 5-save_to_jason_file.py
'''
import json


def save_to_json_file(my_obj, filename):
    ''' function: save_to_json_file
    accepts Python object and sends JSON representation to file
    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
