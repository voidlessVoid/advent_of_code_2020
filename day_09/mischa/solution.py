import os
import sys
import pandas as pd
import numpy as np
import math
import datetime
import operator
from copy import deepcopy
from collections import Counter, ChainMap, defaultdict, deque
from itertools import cycle, combinations
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
    p = 25
    act_num = 25
    for i in inp[act_num:]:
        pre_nums = [int(x) for x in inp[act_num-p:act_num]]
        all_comb = [x for x in combinations(pre_nums,2)]
        count = 0
        for x in all_comb:
            if sum(x) == int(inp[act_num]):
                count+=1
                break
        if count != 1:
            print('answerA: ',inp[act_num])
            return inp[act_num]
        act_num += 1

A = part_a(data)

def part_b(target,inp):
    for idx,i in enumerate(inp):
        curr = int(inp[idx])
        count = idx+1
        temp =[]
        while curr < int(target):
            curr+= int(inp[count])
            if curr == int(target):
                return print('answerB: ', min(temp) + max(temp))
            temp.append(int(inp[count]))
            count+=1

part_b(A,data)

#answerA:  26796446
#answerB:  3353494