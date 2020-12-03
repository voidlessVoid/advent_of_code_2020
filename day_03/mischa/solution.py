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

data = read_input_lines()
def part_a(inp):
    counter = 0
    tree_count=0
    for i in inp:
        temp = i *200
        if temp[counter] == '#':
            tree_count+=1
        counter +=3
    print('part_A',tree_count)
    return tree_count

def part_b(inp,answerA):
    counterA,counterC ,counterD,counterE = 0,0,0,0
    tree_countA,tree_countC,tree_countD,tree_countE  = 0,0,0,0
    for idx,i in enumerate(inp):
        temp = i * 200
        if temp[counterA] == '#':
            tree_countA += 1
        if temp[counterC] == '#':
            tree_countC += 1
        if temp[counterD] == '#':
            tree_countD += 1
        if idx %2==0:
            if temp[int(counterE)] == '#':
                tree_countE += 1
            counterE += 1
        counterA += 1
        counterC +=5
        counterD+=7
    print('part_B', tree_countA*tree_countC*tree_countD*tree_countE*answerA)
A = part_a(data)
part_b(data,A)

