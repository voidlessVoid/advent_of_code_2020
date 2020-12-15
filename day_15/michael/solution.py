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


def solve(upto):
    start = [18, 11, 9, 0, 5, 1]
    lastSpoken = dict(zip(start[:-1], range(1, len(start))))
    last = start[-1]
    for tstep in range(len(start) + 1, upto + 1):
        if last in lastSpoken:
            nextNumber = (tstep - lastSpoken[last]) - 1
        else:
            nextNumber = 0
        lastSpoken[last] = tstep - 1
        last = nextNumber
    print(nextNumber)


def part_a():
    solve(2020)


def part_b():
    solve(30000000)


part_a()
part_b()
