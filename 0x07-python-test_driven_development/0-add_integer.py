#!/usr/bin/python3

"""Return the sum
a and b must be integers or floats,
otherwise raise a TypeError exception
a and b must be first casted to integers if they are float
"""


def add_integer(a, b=98):
    """adds an integer
    unit tests located in tests/0-add_integer.txt
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
