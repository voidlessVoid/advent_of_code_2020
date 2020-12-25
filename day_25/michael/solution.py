import os
import sys
import pandas as pd
import numpy as np
import math
import datetime
import operator
from copy import deepcopy
from collections import Counter, ChainMap, defaultdict, deque
from itertools import cycle
from functools import reduce

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

publics = [12320657,9659666]

def part_a():
    target = 12320657
    value = 1
    subject = 7
    loopnr = 0
    while value != target:
        loopnr +=1
        value *=subject
        value %= 20201227

    print(loopnr)
    subject = 9659666
    value = 1
    for _ in range(loopnr):
        value *= subject
        value %= 20201227

    print(value)

    # too low

part_a()

def part_b():
    pass