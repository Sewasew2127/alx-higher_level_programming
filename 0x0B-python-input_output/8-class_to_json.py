#!/usr/bin/python3
"""
*******************************
Supproting file:8-my_class.py,8-main.py
to run: ./8-main.py
*******************************
"""

def class_to_json(obj):
    """
    a function that returns the dictionary
    description with simple data structure 
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    return vars(obj)
