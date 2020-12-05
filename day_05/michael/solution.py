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

def search(inputstring,min,max,lowtoken,hightoken):
    if inputstring == '':
        return min
    interval = max-min
    if inputstring[0] == lowtoken:
        return search(inputstring[1:],min,min + interval//2,lowtoken,hightoken)
    return search(inputstring[1:], max - interval // 2, max, lowtoken, hightoken)

def getId(seat):
    row = search(seat[:7],0,127,"F","B")
    col = search(seat[7:],0,7,"L","R")
    return row * 8 + col

def part_a():
    seats = read_input_lines()
    print(max([getId(x) for x in seats]))

def part_b():
    seats = read_input_lines()
    ids = {getId(x) for x in seats}
    idsplus1 = {x +1 for x in ids}
    idsminus1 = {x - 1 for x in ids}
    print((idsplus1 & idsminus1) - ids)

part_a()
part_b()