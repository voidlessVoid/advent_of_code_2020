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
from more_itertools import locate
from functools import reduce

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

data = [13,0,10,12,1,5,8]
def part_a():
    while len(data) != 2020:
        last_num = data[-1]
        if last_num not in data[:-1]:
            data.append(0)
        else:
            last_occ = list(locate(data, lambda x: x == last_num))
            next_num = last_occ[-1]-last_occ[-2]
            data.append(next_num)
    print(data[-1])
part_a()
data = [13,0,10,12,1,5,8]
def part_b():
    dict_of_nums = {13:1, 0:2, 10:3, 12:4, 1:5, 5:6, 8:7}
    last_num = data[-1]
    next_num = 0
    step = len(data)+1
    while len(data) != 30000000:
        if last_num not in dict_of_nums:
            next_num = 0
            data.append(0)
        else:
            next_num = (step-dict_of_nums[last_num])-1
            data.append(next_num)
        dict_of_nums[last_num]=step-1
        last_num = next_num
        step+=1
    print(next_num)
part_b()