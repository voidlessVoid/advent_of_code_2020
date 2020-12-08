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

data=read_input_lines()

def part_a(inp):
    acc,pos =0,0
    visited=[]
    while True:
        if pos in visited:
            print('answerA:',acc)
            break
        if 'acc' in inp[pos]:
            visited.append(pos)
            acc += int(re.findall("-?(?:\d+,?)+", inp[pos])[0])
        elif 'jmp' in inp[pos]:
            visited.append(pos)
            pos += int(re.findall("-?(?:\d+,?)+",inp[pos])[0])-1
        elif 'nop' in inp[pos]:
            visited.append(pos)
        pos+=1


def part_b(inp):
    def check_infinity(inp2):
        acc, pos = 0, 0
        visited = []
        while True:
            if pos in visited:
                return False
            if 'acc' in inp2[pos]:
                visited.append(pos)
                acc += int(re.findall("-?(?:\d+,?)+", inp2[pos])[0])
            elif 'jmp' in inp2[pos]:
                visited.append(pos)
                pos += int(re.findall("-?(?:\d+,?)+", inp2[pos])[0]) - 1
            elif 'nop' in inp2[pos]:
                visited.append(pos)
            pos += 1
            if pos >= len(inp2):
                print('answerB:',acc)
                return True
    inf = False
    pos_jmp,pos_nop  = [],[]
    for idx, x in enumerate(inp) :
        if 'jmp' in x:
            pos_jmp.append(idx)
        if 'nop' in x:
            pos_nop.append(idx)

    for x in [pos_nop,pos_jmp]:
        while x and not inf:
            changed_input = deepcopy(inp)
            change = x.pop(0)
            temp = re.findall("-?(?:\d+,?)+", inp[change])[0]
            changed_input[change]= 'nop '+temp
            inf = check_infinity(changed_input)

part_a(data)
part_b(data)

#answerA: 1384
#answerB: 761