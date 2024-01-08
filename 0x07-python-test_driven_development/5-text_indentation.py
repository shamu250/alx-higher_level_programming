#!/usr/bin/python3
'''
module: 5-text_indentation
'''


def text_indentation(text):
    '''break text into lines on punctuation marks

    text: a big (maybe) of text to be broken into pieces ...
    '''

    # TEST/INPUT VALIDATION #
    if type(text) != str:
        raise TypeError("text must be a string")

    delims = {".", "?", ":"}
    white_space = {" ", "\t", "\r"}
    new_line = True

    for ch in text:
        if new_line is True:
            if ch not in white_space:
                print(ch, end='')
                new_line = False
        elif ch in delims:
            print("{}\n".format(ch))
            new_line = True
        else:
            print(ch, end='')
            new_line = False
