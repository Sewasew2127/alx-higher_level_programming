#!/usr/bin/python3

"""
Protototype: def read_file(filename)

"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8)
    and prints it to stdout
    use the with statement
     """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
