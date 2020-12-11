import os
from copy import deepcopy
from collections import defaultdict

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)


def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]


def part_a():
    lines = read_input_lines()
    seatdict = {row + (1j * col): lines[row][col] for row in range(len(lines)) for col in range(len(lines[0]))}
    seatdict = defaultdict(lambda: ".", seatdict)

    deltas = {drow + (1j * dcol) for drow in [-1, 0, 1] for dcol in [-1, 0, 1]} - {0}
    changed = True
    while changed:
        changed = False
        nextdict = defaultdict(lambda: ".", deepcopy(seatdict))

        for loc, symbol in list(seatdict.items()):
            if symbol == "L" and ([seatdict[loc + delta] for delta in deltas].count("#") == 0):
                nextdict[loc] = "#"
                changed = True
            elif symbol == "#" and ([seatdict[loc + delta] for delta in deltas].count("#") > 3):
                nextdict[loc] = "L"
                changed = True

        seatdict = nextdict

    print(list(seatdict.values()).count("#"))


def part_b():
    def get_ajacent(loc, delta, seatdict):
        loc += delta
        while loc in seatdict:
            if seatdict[loc] in "#L":
                return loc
            loc += delta
        return loc

    lines = read_input_lines()
    seatdict = {row + (1j * col): lines[row][col] for row in range(len(lines)) for col in range(len(lines[0]))}
    seatdict = defaultdict(lambda: ".", seatdict)
    deltas = {drow + (1j * dcol) for drow in [-1, 0, 1] for dcol in [-1, 0, 1]} - {0}
    ajacents = {loc: [get_ajacent(loc, delta, seatdict) for delta in deltas] for loc in seatdict}

    changed = True
    while changed:
        changed = False
        nextdict = defaultdict(lambda: ".", deepcopy(seatdict))

        for loc, symbol in list(seatdict.items()):
            visible = [seatdict[x] for x in ajacents[loc]]
            if symbol == "L" and (visible.count("#") == 0):
                nextdict[loc] = "#"
                changed = True
            elif symbol == "#" and (visible.count("#") > 4):
                nextdict[loc] = "L"
                changed = True

        seatdict = nextdict

    print(list(seatdict.values()).count("#"))


part_a()
part_b()
