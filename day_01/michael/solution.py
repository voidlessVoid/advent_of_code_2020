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


def part_a():
    numbers = [int(x) for x in read_input_lines()]
    a,b  = [(x,y) for x in numbers for y in numbers if (x + y) == 2020][0]
    print(a * b)

def part_b():
    numbers = [int(x) for x in read_input_lines()]
    a, b, c = [(x, y, z) for x in numbers for y in numbers  for z in numbers if (x + y + z) == 2020][0]
    print(a * b * c)

part_b()