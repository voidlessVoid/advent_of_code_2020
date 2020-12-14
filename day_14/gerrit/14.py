from itertools import combinations

from data import read_lines
from util import log


real_data = list(read_lines(14))


test_data = [
    "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
    "mem[8] = 11",
    "mem[7] = 101",
    "mem[8] = 0",
]


# ----------------------------------------------------
# Part 1


def from_bin(s):
    return int(s, 2)


def apply_mask(m):
    m_plus = from_bin("".join([
        "1" if c == "1" else "0"
        for c in m
    ]))
    m_minus = from_bin("".join([
        "0" if c == "0" else "1"
        for c in m
    ]))

    return lambda n: (
        (n | m_plus) & m_minus
    )


# Unit test apply_mask


inp    = from_bin("111000")
mask   =          "X10X10"
target = from_bin("110010")


assert apply_mask(mask)(inp) == target


def part_1(data):
    mem = {}
    mask = lambda n: n

    for line in data:
        if line.startswith("mask"):
            mask = apply_mask(line.split(" = ")[1])
        else:
            assert line.startswith("mem")

            cmd, num = line.split("] = ")
            index    = cmd.split("[")[1]

            mem[index] = mask(int(num))

    return sum(mem.values())


assert part_1(test_data) == 165


print(part_1(real_data))


# ----------------------------------------------------
# Part 2

test_data_2 = [
    "mask = 000000000000000000000000000000X1001X",
    "mem[42] = 100",
    "mask = 00000000000000000000000000000000X0XX",
    "mem[26] = 1",
]

def subsets(items):
    item_set = set(items)

    for size in range(len(item_set) + 1):
        for s in combinations(item_set, size):
            yield s


def address_range(mask):
    marked_indices = [
        index
        for index, c in enumerate(mask)
        if c == "X"
    ]

    modify = lambda index, sub: (
        "1" if index in sub else "0"
    )

    modification_masks = [
        [
            modify(index, sub) if index in marked_indices else "X"
            for index in range(len(mask))
        ]
        for sub in subsets(marked_indices)
    ]

    force_ones = from_bin("".join([
        "1" if c == "1" else "0"
        for c in mask
    ]))

    def fn(addr):
        return [
            apply_mask(modification)(force_ones | int(addr))
            for modification in modification_masks
        ]

    return fn


def part_2(data):
    mem = {}
    address_mask = None

    for line in data:
        if line.startswith("mask"):
            address_mask = address_range(line.split(" = ")[1])
        else:
            assert line.startswith("mem")

            cmd, num = line.split("] = ")
            index    = cmd.split("[")[1]

            for addr in address_mask(index):
                mem[addr] = int(num)

    return sum(mem.values())


assert part_2(test_data_2) == 208


print(part_2(real_data))


# print(set(subsets([1, 2, 3])))
