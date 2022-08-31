#!/usr/bin/python3
"""
*******************************
Supproting file: my_fake.json,
                my_list.json.6-main.py
to run: ./6-main.py
*******************************
"""

import json


def load_from_json_file(filename):
    """
    function that creates an Object from
    a “JSON file”
    """
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
