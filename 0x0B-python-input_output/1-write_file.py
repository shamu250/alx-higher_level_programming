#!/usr/bin/python3
''' module 3-write_file
'''


def write_file(filename="", text=""):
    '''function: write_file
    accepts filename and text string to write to file
    '''
    if filename == "" or type(filename) != str:
        return
    if type(text) != str:
        return
    with open(filename, 'w') as f:
        nb_chars = f.write(text)
        f.close()
    return nb_chars
