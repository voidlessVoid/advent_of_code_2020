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
    lines = read_input_lines()
    height, width = len(lines), len(lines[0])
    print(sum([lines[row][(row*3)%width] == '#' for row in range(height)]))

def part_b():
    lines = read_input_lines()
    height, width = len(lines), len(lines[0])
    ans = 1
    for drow, dcol in [(1,1),(1,3),(1,5),(1,7),(2,1)]:
        ans *= sum([lines[step * drow][(step * dcol) % width] == '#' for step in range(((height-1)//drow)+1)])

    print(ans)

part_a()
part_b()