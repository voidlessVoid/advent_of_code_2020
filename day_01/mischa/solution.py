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
data=read_input_lines()
df = pd.DataFrame(data, columns=['nums'])



def part_a(inp):
    for i in inp['nums']:
        temp = inp.add(i)
        if 2020 in temp['nums'].values:
            return print('answerA', (2020 - i) * i)


def part_b(inp):
    for i in inp['nums']:
        temp = inp.add(i)
        temp1 = temp[temp.nums <2020]
        for x in inp['nums']:
            temp2 = temp1.add(x)
            if 2020 in temp2['nums'].values:
                return print('answerB', (i*x*(2020-i-x)))
part_a(df)
part_b(df)
#answerA 437931
#answerB 157667328
