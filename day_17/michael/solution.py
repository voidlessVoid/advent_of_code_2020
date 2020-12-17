import os
from copy import deepcopy
from collections import defaultdict

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    def getAjacent(loc):
        x,y,z = loc
        deltas = [-1,0,1]
        steps = {(dx,dy,dz) for dx in deltas for dy in deltas for dz in deltas} - {(0,0,0)}
        return {(x+dx,y+dy,z+dz) for dx,dy,dz in steps}

    lines =  read_input_lines()
    active = {(x,y,0) for y in range(len(lines)) for x in range(len(lines[0])) if lines[y][x] == "#"}

    for _ in range(6):
        counts = defaultdict(int)
        for loc in active:
            for ajacent in getAjacent(loc):
                counts[ajacent] +=1

        nextCycleActive = set()
        for ajacent, c in counts.items():
            if c == 3:
                nextCycleActive.add(ajacent)
            elif (c == 2) and (ajacent in active):
                nextCycleActive.add(ajacent)

        active = nextCycleActive

    print(len(active))

def part_b():
    def getAjacent(loc):
        x, y, z, a = loc
        deltas = [-1, 0, 1]
        steps = {(dx, dy, dz, da) for dx in deltas for dy in deltas for dz in deltas for da in deltas} - {(0, 0, 0, 0)}
        return {(x + dx, y + dy, z + dz, a + da) for dx, dy, dz, da in steps}

    lines = read_input_lines()
    active = {(x, y, 0, 0) for y in range(len(lines)) for x in range(len(lines[0])) if lines[y][x] == "#"}

    for _ in range(6):
        counts = defaultdict(int)
        for loc in active:
            for ajacent in getAjacent(loc):
                counts[ajacent] += 1

        nextCycleActive = set()
        for ajacent, c in counts.items():
            if c == 3:
                nextCycleActive.add(ajacent)
            elif (c == 2) and (ajacent in active):
                nextCycleActive.add(ajacent)

        active = nextCycleActive

    print(len(active))

part_a()
part_b()