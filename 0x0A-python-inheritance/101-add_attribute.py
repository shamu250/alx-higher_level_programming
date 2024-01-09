#!/usr/bin/python3

"""
Module: attribute_manager
Description: This module provides a function for adding attributes to objects
             while enforcing a restriction on objects with an existing docstring.
"""

def add_attribute(obj, attribute_name, value):
    """
    Function: add_attribute
    Description: Adds a new attribute to the given object if it doesn't have a docstring.
                 Raises a TypeError if the object already has a docstring.
    Parameters:
        - obj: The object to which the attribute should be added.
        - attribute_name: The name of the attribute to be added.
        - value: The value of the attribute to be added.
    Raises:
        - TypeError: If the object already has a docstring.
    """
    existing_docstring = getattr(obj, "__doc__", None)
    if existing_docstring is None:
        setattr(obj, attribute_name, value)
    else:
        raise TypeError("Can't add new attribute to objects with an existing docstring")
