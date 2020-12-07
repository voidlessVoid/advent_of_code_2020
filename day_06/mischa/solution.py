import os
import sys
import pandas as pd
import numpy as np
import math
import datetime
import operator
from copy import deepcopy
from collections import Counter, ChainMap, defaultdict, deque
from itertools import cycle, chain
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

def make_dict(input_list):
    dict_temp = defaultdict()
    next_key = 0
    for line in input_list:
        if len(line.strip()) == 0:
            next_key += 1
        else:
            temp = line.split()
            for field in temp:

                if str(next_key) in dict_temp.keys():
                    dict_temp[str(next_key)].append(line)
                else:
                    dict_temp[str(next_key)] = ([])
                    dict_temp[str(next_key)].append((line))
    return dict_temp

def make_dict_set(input_list):
    dict_temp = defaultdict()
    next_key = 0
    for line in input_list:
        if len(line.strip()) == 0:
            next_key += 1
        else:
            temp = line.split()
            for field in temp:

                if str(next_key) in dict_temp.keys():
                    dict_temp[str(next_key)].append(set(line))
                else:
                    dict_temp[str(next_key)] = ([])
                    dict_temp[str(next_key)].append((set(line)))
    return dict_temp


def part_a(inp):
    dict_of_groups = make_dict(inp)
    sum_of_groups =0
    for i in dict_of_groups:
        flat = chain.from_iterable(dict_of_groups[i])
        sum_of_groups += len(set(list(flat)))
    print('answerA: ',sum_of_groups)




def part_b(inp):
    dict_of_groups = make_dict_set(inp)
    list_of_sets = []
    for i in dict_of_groups:
        group_number = len(dict_of_groups[i])
        for x in range(group_number):
            temp_b = (dict_of_groups[i][0]).intersection_update(dict_of_groups[i][x])
        list_of_sets.append(dict_of_groups[i][0])
        answerB = [len(x) for x in list_of_sets]
    print('answerB: ',sum(answerB))


part_a(data)
part_b(data)

#answerA:  6625
#answerB:  3360