#!/usr/bin/python3

"""
function: add_integer
arguments: 2
    a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
unit tests located in tests/0-add_integer.txt
checks for type errors
"""


def add_integer(a, b=98):
    """
    adds an integer
    unit tests located in tests/0-add_integer.txt
    checks for type errors
    """
    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
