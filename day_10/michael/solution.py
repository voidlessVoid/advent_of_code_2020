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
    numbers = [0] + sorted([int(x) for x in read_input_lines()])
    differenceCounts = Counter([numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)])
    print(differenceCounts[1] * (differenceCounts[3] + 1))


def part_b():
    """ differences of 3 are like checkpoints where only one option is present
    here total permutations = permutations left * permutations right"""

    def calcPermute(numbers):
        return calcPermuteHelper(set(numbers), set(), numbers[0], numbers[-1])

    def calcPermuteHelper(numbers, visited, current, goal):
        if current == goal:
            return 1
        visited = deepcopy(visited)
        visited.add(current)
        next_options = ({current - x for x in [-2, -1, 1, 2, 3]} & numbers) - visited
        return sum(calcPermuteHelper(numbers, visited, x, goal) for x in next_options)

    def solve(numbers):
        try:
            nextdelta3ix = next((i for i in range(1, len(numbers)) if numbers[i] - numbers[i - 1] == 3))
            return calcPermute(numbers[:nextdelta3ix]) * solve(numbers[nextdelta3ix:])
        except StopIteration:
            return calcPermute(numbers)

    numbers = [0] + sorted([int(x) for x in read_input_lines()])

    print(solve(numbers))

part_a()
part_b()
