#!/usr/bin/python3
"""
*******************************
Supproting file:
to run: 
*******************************
"""

class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)