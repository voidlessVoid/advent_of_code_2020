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
        return [[x.strip()] for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()
data = read_input_lines()
print(data)

neighbours=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
def part_a(inp):
    for idy,y in enumerate(inp):
        for idx,x in enumerate(y):
            print(x,idy,idx)
            try:
                seat = inp[idx][idy]
                count = 0
                for pos in neighbours:
                    print(idx+pos[0],idy+pos[1])
                    try:
                        neig = inp[idx+pos[0]][idy+pos[1]]
                        if neig == '#':
                            count+=1
                    except:
                        pass
                if seat=='L' and count == 0:
                    inp[idx][idy] = '#'
                if seat == '#' and count >= 4:
                    inp[idx][idy] = 'L'
            except:
                pass

    return inp
new = part_a(data)
print(data)
print(new)
def part_b():
    pass