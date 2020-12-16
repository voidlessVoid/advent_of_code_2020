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
        return [int(x.strip()) for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

data = read_input_lines()

def part_a(inp):
    a,b=[],[]
    temp = sorted(inp)
    for idx ,x in enumerate(temp):
        if int(idx)<len(inp):
            if temp[idx] - temp[idx - 1] == 1:
                a.append(x)
            if temp[idx] - temp[idx - 1] == 3:
                b.append(x)
    print((len(a)+1)*(len(b)+1))

part_a(data)

def part_b():
    pass
