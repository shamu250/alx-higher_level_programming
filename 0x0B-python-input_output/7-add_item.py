#!/usr/bin/python3
''' module: 9-add_item
'''
import json
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    py_list = load_from_json_file(filename)
except FileNotFoundError:
    py_list = []
finally:
    for el in sys.argv[1:]:
        py_list.append(str(el))
    save_to_json_file(py_list, filename)
