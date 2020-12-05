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

def check_if_valid(list_of_fields):
    if len(list_of_fields) == 7 and 'cid' not in list_of_fields:
        return True
    elif len(list_of_fields) == 8:
        return True

def check_if_valid2(list_of_fields):

    for field in list_of_fields:
        if field[0] == 'byr':#done
            if  1920 <= int(field[1]) <= 2002:
                pass
            else:
                return False

        elif field[0] == 'iyr':#done
            if  2010 <= int(field[1]) <= 2020:
                pass
            else:
                return False

        elif field[0] == 'eyr':#done
            if 2020 <= int(field[1]) <= 2030:
                pass
            else:
                return False

        elif field[0] == 'hgt':#done
            if  field[1][-2:] =='cm' and 150 <= int(field[1][:-2]) <= 193:
                pass
            elif field[1][-2:] =='in' and 59 <= int(field[1][:-2]) <= 76:
                pass
            else:
                return False

        elif field[0] == 'hcl':#done
            match = re.search("\A#",field[1])
            match1 = re.search("[0-9a-z]{5}$",field[1])
            if match and match1 :
                pass
            else:
                return False

        elif field[0] == 'ecl':#done
            if field[1] in ['amb','blu','brn','gry','grn','hzl','oth']:
                pass
            else:
                return False

        elif field[0] == 'pid':#done
            match = re.search("[0-9]{9}", field[1])
            if match and len(field[1])==9:
                pass
            else:
                return False
    return True





def part_a(inp):
    dict_of_pass = defaultdict()
    next_key = 0
    for line in inp:
        if len(line.strip()) == 0:
            next_key += 1
        else:
            temp = line.split()
            for field in temp:
                temp_key, temp_value = field.split(':')
                if str(next_key) in dict_of_pass.keys():
                    dict_of_pass[str(next_key)].append((temp_key))
                else:
                    dict_of_pass[str(next_key)] = ([])
                    dict_of_pass[str(next_key)].append((temp_key))
    valid_passes = 0
    valid_pass_list = []
    for x in dict_of_pass:
        if check_if_valid(dict_of_pass[x]) == True:
            valid_passes += 1
            valid_pass_list.append(x)
    print('answerA: ',valid_passes)
    return valid_pass_list


def part_b(inp,valid):
    dict_of_pass = defaultdict()
    next_key = 0
    for line in inp:
        if len(line.strip()) == 0:
            next_key += 1
        else:
            temp = line.split()
            for field in temp:
                temp_key, temp_value = field.split(':')
                if str(next_key) in dict_of_pass.keys():
                    dict_of_pass[str(next_key)].append((temp_key,temp_value))
                else:
                    dict_of_pass[str(next_key)] = ([])
                    dict_of_pass[str(next_key)].append((temp_key,temp_value))
    valid_passes = 0

    for x in dict_of_pass:

        if x in valid and check_if_valid2(dict_of_pass[x]) == True:
            valid_passes += 1


    print('answerB: ',valid_passes)

valid_pass_list1 = part_a(data)
part_b(data,valid_pass_list1)

#answerA:  190
#answerB:  121