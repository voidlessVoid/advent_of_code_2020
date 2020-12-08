import os
from copy import deepcopy

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)


def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]


def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    funcs = {
        "acc": lambda x: (ix + 1, acc + int(x)),
        "jmp": lambda x: (ix + int(x), acc),
        "nop": lambda x: (ix + 1, acc)
    }

    lines = read_input_lines()
    acc = 0
    ix = 0
    visited = set()

    while ix not in visited:
        visited.add(ix)
        op, num = lines[ix].split()
        ix, acc = funcs[op](num)

    print(acc)


def part_b():
    lines = read_input_lines()

    swaps = {"nop": "jmp",
             "jmp": "nop"}

    def solve(visited, ix, acc, changedInstruction):
        funcs = {
            "acc": lambda x: (ix + 1, acc + int(x)),
            "jmp": lambda x: (ix + int(x), acc),
            "nop": lambda x: (ix + 1, acc)
        }

        while ix not in visited:
            if ix == len(lines):
                print(acc)
                return True

            visited.add(ix)
            op, num = lines[ix].split()

            if (not changedInstruction) and op in swaps:
                ixSwap, accSwap = funcs[swaps[op]](num)
                if solve(deepcopy(visited), ixSwap, accSwap, True):
                    return

            ix, acc = funcs[op](num)

    solve(set(), 0, 0, False)


part_a()
part_b()
