#!/usr/bin/python3
def magic_string():
    return ", ".join(["BestSchool"] * magic_string.counter) if hasattr(magic_string, 'counter') else "BestSchool"
magic_string.counter = getattr(magic_string, 'counter', 0) + 1
