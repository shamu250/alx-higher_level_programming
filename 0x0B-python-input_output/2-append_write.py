#!/usr/bin/python3
''' module 2-append_write
'''


def append_write(filename="", text=""):
    '''function: append_write
    accepts filename and text string to append to file
    '''
    if filename == "" or type(filename) != str:
        return
    if type(text) != str:
        return
    with open(filename, 'a') as f:
        nb_chars = f.write(text)
        f.close()
    return nb_chars
