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
pw_valid = []
pw_valid2 = []

def part_a(inp):
    for i in inp:
        lo, hi = re.findall('[0-9]+', i)
        temp = i.split(':')
        key_letter = temp[0][-1]
        pw = temp[1]
        occ = pw.count(key_letter)
        if occ <= int(hi) and occ >= int(lo):
            pw_valid.append(i)
    print('answer_partA: ',len(pw_valid))

def part_b(inp):
    for i in inp:
        lo, hi = re.findall('[0-9]+', i)
        temp = i.split(':')
        key_letter = temp[0][-1]
        pw = temp[1].strip()
        if pw[int(lo)-1] in key_letter and pw[int(hi)-1] not in key_letter \
                or pw[int(lo)-1] not in key_letter and pw[int(hi)-1] in key_letter:
            pw_valid2.append(i)
    print('answer_partB: ', len(pw_valid2))

part_a(data)
part_b(data)
#answer_partA:  445
#answer_partB:  491
