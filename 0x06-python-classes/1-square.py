#!/usr/bin/python3


"""
a class named Square that defines a square based on 0-square.py
class Square has attributes:
    size
"""


class Square:
    """
    the __init__ method run as soon as an object of a class is created.
    It is useful to do ay initialization
    """
    def __init__(self, size):
        """
        the initialization function for the square class
        """
        self.__size = size
