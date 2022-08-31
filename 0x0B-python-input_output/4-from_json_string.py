#!/usr/bin/python3
"""
*******************************
Supproting file: 4-main.py
to run: ./4-main.py
*******************************
"""


import json


def from_json_string(my_str):
    """
    a function that returns 
    an object (Python data structure)
    represented by a JSON string
    """
    return json.loads(my_str)
