from itertools import combinations

from util import apply_to, compose

from data import read_lines


real_data = list(read_lines(9))


test_data = [
    "35",
    "20",
    "15",
    "25",
    "47",
    "40",
    "62",
    "55",
    "65",
    "95",
    "102",
    "117",
    "150",
    "182",
    "127",
    "219",
    "299",
    "277",
    "309",
    "576",
]


def as_ints(data):
    return [int(x) for x in data]


def windows(data, size):
    for x in range(size, len(data)):
        yield [data[x], data[x-size:x]]


def is_sum_of(x, xs):
    return any(
        x == a + b
        for a, b in combinations(xs, 2)
    )


def part_1(data, size):
    for index, item in enumerate(windows(as_ints(data), size)):
        x, window = item

        if not is_sum_of(x, window):
            return x

    return None


def subsequences(items):
    for index in range(len(items) + 1):
        for start in range(index):
            yield items[index-start-1:index]


def part_2(data, size):
    int_data = as_ints(data)

    target = part_1(int_data, size)

    for subs in subsequences(int_data):
        if target == sum(subs):
            return min(subs) + max(subs)


assert part_1(test_data, 5) == 127
assert part_1(real_data, 25) == 217430975


print(part_1(real_data, 25))


assert part_2(test_data, 5) == 62
assert part_2(real_data, 25) == 28509180


print(part_2(real_data, 25))
