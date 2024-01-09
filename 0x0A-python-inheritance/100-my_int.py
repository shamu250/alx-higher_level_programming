#!/usr/bin/python3

"""
Module: my_int_extension
Description: This module defines a custom integer class, MyInt, with overridden
             equality and inequality methods to provide a different behavior.
"""

class MyInt(int):
    """
    Class: MyInt
    Description: Custom integer class that extends the built-in int class.
                 Overrides the equality and inequality methods for a unique behavior.
    """

    def __eq__(self, other):
        """
        Method: __eq__
        Description: Override the equality method to check if the difference between
                     self and other is not equal to zero.
        Parameters:
            - other: The other object to compare with.
        Returns:
            - bool: True if the difference is not equal to zero, False otherwise.
        """
        return self - other != 0

    def __ne__(self, other):
        """
        Method: __ne__
        Description: Override the inequality method to check if the difference between
                     self and other is equal to zero.
        Parameters:
            - other: The other object to compare with.
        Returns:
            - bool: True if the difference is equal to zero, False otherwise.
        """
        return self - other == 0
