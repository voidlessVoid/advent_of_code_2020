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
import re

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()
data = read_input_lines()
rules = [x.split(':') for x in data if re.findall("[a-z]",x) and re.findall("[0-9]",x)]
temp = []
nearby_tickets2 = [x.split(',') for x in [x for x in data if re.findall("^[0-9]+",x)][1:]]
for i in nearby_tickets2:
    for x in i:
        temp.append(int(x))

def part_a():
    valid_nums = []
    invalid_nums = []
    for rule in rules:
        limits = re.findall("[0-9]+",rule[1])
        temp1 = [valid_nums.append(int(x)) for x in range(int(limits[0]),int(limits[1])+1)]
        temp2 = [valid_nums.append(int(x)) for x in range(int(limits[2]),int(limits[3])+1)]
    for i in temp:
        if i not in valid_nums:
            invalid_nums.append(i)
    print(sum(invalid_nums))

part_a()
def part_b():
    pass