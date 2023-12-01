#!/usr/bin/python3
def no_c(my_string):
    return "".join([elem for elem in my_string
                    if elem != "c" and elem != "C"])
