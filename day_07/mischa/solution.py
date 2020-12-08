import os
import sys
import pandas as pd
import numpy as np
import logging
import math
import datetime
import operator
from copy import deepcopy
from collections import Counter, ChainMap, defaultdict, deque
from itertools import cycle
from functools import reduce
import re
logger = logging.getLogger('ftpuploader')

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
    print('children1',children)

    for i in children:
        if act_bag == 'shinygold':
            dict_of_bags[act_bag][0].append(str(1))
            print('children2', children)
        elif 'no' not in i:

            print('mult ', mult)
            print(i[-1])
            dict_of_bags[act_bag][0].append(str(mult))
            dict_of_bags[act_bag][0][-1]=int(dict_of_bags[act_bag][0][-1])*int(mult)
            print(dict_of_bags[act_bag])
            print('children3', children)
            num = int(i[-1]) * int(mult)
    sum_childs = sum([int(x[0]) for x in children if 'no' not in x])
    temp_sum = sum_childs*int(mult)
    bags_in_gold += temp_sum
    print('sum_childs',sum_childs)
    print('multiplikator',mult)

    for x in children:
        if 'no' not in x:
            bags_to_visit.append(''.join(x[:-1]))
            print('num_of_bags',x[0])
            print('multiplikator',mult)
        else:
            pass

    if len(bags_to_visit) > 0:
        print('t',bags_to_visit[-1])
        mult = re.findall("[0-9]+",bags_to_visit[-1])[0] ##mult is always 2 has to change

        print('found mult', mult)
        act_bag = re.findall("[a-z]+",bags_to_visit.pop(-1))[0]
        print('next_bag')
        print(act_bag)

    else:
        print('done')
        print(bags_in_gold)
        return bags_in_gold
    traverse2(act_bag,valid_bags,bags_to_visit,bags_in_gold,mult)

def traverse3(act_bag,valid_bags,bags_to_visit,bags_in_gold,mult):
    children = dict_of_bags[act_bag]
    print('')
    print('act_bag',act_bag)
    print('children1',children)
    if act_bag == 'shinygold':
        dict_of_bags[act_bag][0].append(str(1))
        print('children2', children)


    print(dict_of_bags[act_bag])
    mult = int(dict_of_bags[act_bag][0][-1])#somehow this is the number of bags not the multiplier. if i change stuff in the file it doesnt change the results here
    print('mult',mult)
    for x in children:
        print('x',x)
        if dict_of_bags[''.join(x[1:3])][0][0] =='no':
            print('foundError')
        else:#for every child add the mult in the dict of bags
            try: # the contains no bag bag throughs an error i have to calculate its amount but have to stop there
                dict_of_bags[''.join(x[1:3])][0].append(str(mult * int(dict_of_bags[''.join(x[1:3])][0][0])))
                bags_to_visit.append(''.join(x[1:3]))
            except Exception as e:  # work on python 3.x
                logger.error('Failed to upload to ftp: ' + str(e))

    if len(bags_to_visit) > 0  :
        act_bag = re.findall("[a-z]+",bags_to_visit.pop(-1))[0]
    else:
        return bags_in_gold
    traverse3(act_bag,valid_bags,bags_to_visit,bags_in_gold,mult)

def part_b_2():
    bags_in_gold =0
    valid_bags = []
    bags_to_visit = []
    multiplikator=1

    test = traverse3('shinygold', valid_bags, bags_to_visit, bags_in_gold,multiplikator)
    print('answerB: ',bags_in_gold, test)
    print(dict_of_bags)

part_b_2()

def part_b():
    bags_in_gold =0
    valid_bags = []
    bags_to_visit = []
    multiplikator=1
    test = traverse2('shinygold', valid_bags, bags_to_visit, bags_in_gold,multiplikator)
    print('answerB: ',bags_in_gold, test)


#171 too low


