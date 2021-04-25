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

    with open(fname, 'r') as f:
        info = json.load(f)
    return info['root']


def get_random_tip(data=info):
    """
    Randomly selects a tip dictionary from the given sequence.
    """

    return random.choice(info)


# Load on import
try:
    info = read_file()
except Exception as e:
    print(e)
