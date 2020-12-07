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
    with open('fake_input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


data = read_input_lines()
def make_tree(inp):
    dict_of_bags = defaultdict()
    for line in inp: #make tree
        line=line.replace('contain','')
        line=line.replace('bags','bag')
        line=line.replace(',','')
        line=line[:-1]
        temp = line.split('bag')[:-1]
        dict_of_bags[temp[0].strip().replace(' ','')] = [re.findall(r"\w+",x) for x in temp[1:]]
    return dict_of_bags

def traverse(act_bag,valid_bags,bags_to_visit):
    children = dict_of_bags[act_bag]
    for x in children:
        if 'shiny' in x and 'gold' in x:
            valid_bags.append(act_bag)
            return True
        else:
            if 'no' not in x:
                bags_to_visit.add(''.join(x[1:]))
    if len(bags_to_visit)>0:
        act_bag = bags_to_visit.pop()
    else:
        return False
    traverse(act_bag,valid_bags,bags_to_visit)

def part_a(tree):
    valid_bags= []
    visited_bags= []
    for i in tree:
        bags_to_visit = set()
        visited_bags.append(i)
        test = traverse(i,valid_bags,bags_to_visit)
    print('answerA: ',len(valid_bags))

dict_of_bags = make_tree(data)
part_a(dict_of_bags)
#answerA:  355

#### part 2 is still a mess... ####
def traverse2(act_bag,valid_bags,bags_to_visit,bags_in_gold,mult):
    children = dict_of_bags[act_bag]
    print('')
    print('act_bag',act_bag)
    print('children',children)
    sum_childs = sum([int(x[0]) for x in children if 'no' not in x])
    temp_sum = sum_childs*int(mult)
    bags_in_gold += temp_sum
    print('sum_childs',sum_childs)
    print('multiplikator',mult)
    for x in children:
        if 'no' not in x:
            bags_to_visit.append(''.join(x[1:]))
            mult = x[0]
            print('num_of_bags',x[0])
            print('multiplikator',mult)
        else:
            mult = 1
    if len(bags_to_visit)>0:
        act_bag = bags_to_visit.pop(-1)
        print('next_bag')
        print(act_bag)

    else:
        print('done')
        print(bags_in_gold)
        return bags_in_gold
    traverse2(act_bag,valid_bags,bags_to_visit,bags_in_gold,mult)

def part_b():
    bags_in_gold =0
    valid_bags = []
    bags_to_visit = []
    multiplikator=1
    test = traverse2('shinygold', valid_bags, bags_to_visit, bags_in_gold,multiplikator)
    print('answerB: ',bags_in_gold, test)
part_b()

#171 too low


