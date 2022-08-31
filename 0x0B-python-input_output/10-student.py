#!/usr/bin/python3
"""
*******************************
Supproting file:1-0main.py
to run: ./10-main.py
*******************************
"""


class Student:
    """
    a function that reads a text file (UTF8)
    and prints it to stdout
    use the with statement
    """

    def __init__(self, first_name, last_name, age):
        """
        a function that reads a text file (UTF8)
        and prints it to stdout
        use the with statement
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        a function that reads a text file (UTF8)
        and prints it to stdout
        use the with statement
        """
        if attrs is None:
            return self.__dict__
        new_dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dictionary[key] = value
        return new_dictionary
