#!/usr/bin/python3


"""
*******************************
Supproting file:1-main.py
to run: ./1-main.py
*******************************
"""


def write_file(filename="", text=""):
    """
    a function that writes a string
    to a text file (UTF8) and returnst
    the number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
