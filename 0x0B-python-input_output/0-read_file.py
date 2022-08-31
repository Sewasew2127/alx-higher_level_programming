#!/usr/bin/python3

"""
*******************************
Supproting file: 0-main.py
to run:./0-main.py 
*******************************
"""

def read_file(filename=""):
    """
    a function that reads a text file (UTF8)
    and prints it to stdout
    use the with statement
     """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
