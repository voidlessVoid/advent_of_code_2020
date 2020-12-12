from functools import reduce

from util import (
    as_ints,
    split_by,
    apply_to,
    compose,
    map
)

from data import read_lines


real_data = list(read_lines(10))


test_data_1 = [
    "16",
    "10",
    "15",
    "5",
    "1",
    "11",
    "7",
    "19",
    "6",
    "12",
    "4",
]


test_data_2 = [
    "28",
    "33",
    "18",
    "42",
    "31",
    "14",
    "46",
    "20",
    "48",
    "47",
    "24",
    "23",
    "49",
    "45",
    "19",
    "38",
    "39",
    "11",
    "1",
    "32",
    "25",
    "35",
    "8",
    "17",
    "7",
    "9",
    "4",
    "2",
    "34",
    "10",
    "3",
]


def gaps(ints):
    latest = None
    for x in ints:
        if latest != None:
            yield x - latest
        latest = x


def part_1(data):
    gap_counts = reduce(
        lambda acc, gap: {
            **acc,
            gap: acc.get(gap, 0) + 1
        },
        gaps(sorted([0, *as_ints(data)])),
        { 3: 1 }
    )

    return gap_counts[1] * gap_counts[3]


assert part_1(test_data_1) == 7 * 5
assert part_1(test_data_2) == 22 * 10


# print(part_1(real_data))


def log(x):
    print(x)
    return x


def combinations(length):
    if length <= 0:
        return 1

    res = sum(
        combinations(length - (i + 1))
        for i in range(min(length, 3))
    )

    # print(length, res, [
    #     length - (i + 1)
    #     for i in range(min(length, 3))
    # ])

    return res

# print(combinations(4))
# print(combinations(3))
# print(combinations(2))
# print(combinations(1))


def part_2(data):
    partial_solutions = apply_to(data, compose(
        lambda d: [0, *as_ints(d)],
        sorted,
        gaps,
        split_by(lambda x: x == 3),
        map(len),
        map(combinations)
    ))

    return reduce(lambda x, y: x*y, partial_solutions, 1)
    # return list(partial_solutions)


assert part_2(test_data_1) == 8
assert part_2(test_data_2) == 19208


print(part_2(real_data))

# print(reduce(lambda x, y: x*y, [4, 7, 4, 2, 7, 1, 7], 1))
