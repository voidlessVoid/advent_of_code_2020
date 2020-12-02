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


def part_a():

    def check_line(line):
        rule, password = [x.strip() for x in line.split(":")]
        freq, char = rule.split()
        minfreq, maxfreq = [int(x) for x in freq.split("-")]
        return minfreq <= password.count(char) <= maxfreq

    print(sum([check_line(x) for x in read_input_lines()]))


def part_b():
    def check_line(line):
        rule, password = [x.strip() for x in line.split(":")]
        freq, char = rule.split()
        ixes = [int(x) - 1 for x in freq.split("-")]
        return "".join([password[ix] for ix in ixes]).count(char) == 1

    print(sum([check_line(x) for x in read_input_lines()]))

part_a()
part_b()