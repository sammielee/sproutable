# File: greentips.py

import json
import random


# File management
default_file = 'data/greentips_data.json'
current_file = default_file


# The master list of tips
info = [None]


def read_file(fname=current_file):
    """
    Ideally reads the .json file with the proper format. This should yield an
    iterable of smaller dictionaries with 'header' and 'data' keys.
    """

    data = {}
    with open(fname, 'r') as f:
        data = json.load(f)
    return data['root']


def get_random_tip(data=info):
    """
    Randomly selects a tip dictionary from the given sequence.
    """

    return random.choice(info)


# Load on import
info = read_file()
