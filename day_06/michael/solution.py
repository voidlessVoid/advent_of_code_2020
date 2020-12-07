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
    grouptexts = read_input_text().split("\n\n")
    groupconcats = [x.replace("\n","") for x in grouptexts]
    print(sum([len(set(x)) for x in groupconcats]))

def part_b():
    grouptexts = read_input_text().split("\n\n")
    linesAsSets = [[set(y) for y in x.split()] for x in grouptexts]
    print(sum([len(reduce(operator.__and__, x )) for x in linesAsSets]))

part_a()
part_b()
3382