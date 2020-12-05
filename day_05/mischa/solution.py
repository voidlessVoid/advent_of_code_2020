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
seat_list = [x for x in range(128)]
def divide_row(row_id):
    temp = deepcopy(seat_list)
    for x in row_id:
        med = len(temp)//2 #thanks michael for reminding me :)
        if x =='F':
            temp = temp[:med]
        elif x=='B':
            temp = temp[med:]
    return temp
def divide_window_place(col_id):
    temp = [x for x in range(8)]
    for x in col_id:
        med = len(temp) // 2  # thanks michael for reminding me :)
        if x == 'L':
            temp = temp[:med]
        elif x == 'R':
            temp = temp[med:]
    return temp

def part_a(inp):
    list_seat_id = []
    for i in inp:
        row_id,col_id = i[:-3], i[-3:]
        row_num = divide_row(row_id)
        column_num = divide_window_place(col_id)
        seat_id = row_num[0]*8+column_num[0]
        list_seat_id.append(int(seat_id))
    list_seat_id.sort()
    print('answerA:', list_seat_id[-1])
    return list_seat_id



def part_b(inp):
    pos_seats= [x for x in range(979) if x not in [x for x in range(13)]]
    B = set(inp).symmetric_difference(set(pos_seats))
    print('answerB: ',B)
a = part_a(data)
part_b(a)
