import os
from collections import Counter, ChainMap, defaultdict, deque

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)


def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]


def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


mapping = {"w": -1, "e": 1, "nw": 1j, "se": -1j, "ne": 1 + 1j, "sw": -1 * (1 + 1j)}


def toCoords(instring):
    pos = 0
    i = 0
    while i < len(instring):
        if instring[i] in mapping:
            pos += mapping[instring[i]]
            i += 1
        else:
            pos += mapping[instring[i:i + 2]]
            i += 2

    return pos


def part_a():
    inputs = read_input_lines()
    print(len([x for x in Counter([toCoords(inp) for inp in inputs]).values() if (x % 2) == 1]))


def part_b():
    inputs = read_input_lines()
    blackPos = {k for k, v in Counter([toCoords(inp) for inp in inputs]).items() if (v % 2) == 1}

    for _ in range(100):
        toWhite = {pos for pos in blackPos if
                   len(({pos + delta for delta in mapping.values()} & blackPos)) not in [1, 2]}

        allAjacent = {pos + delta for pos in blackPos for delta in mapping.values()}
        toBlack = {pos for pos in allAjacent if len(({pos + delta for delta in mapping.values()} & blackPos)) == 2}
        toBlack -= blackPos  # this rule is only for tiles that were white

        blackPos -= toWhite
        blackPos |= toBlack

    print(len(blackPos))


part_b()
