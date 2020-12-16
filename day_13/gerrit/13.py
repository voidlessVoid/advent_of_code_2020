from math import ceil

from data import read_lines

from util import (
    apply_to,
    compose,
    filter_with,
    minimum_by,
    map,
    prod,
    unzip,
)


real_data = list(read_lines(13))


test_data = [
    "939",
    "7,13,x,x,59,x,31,19",
]


def earliest_after(start):
    return lambda period: (
        ceil(start / period) * period
    )


def part_1(data):
    start = int(data[0])

    return apply_to(data[1], compose(
        lambda d: d.split(","),
        filter_with(lambda item: item != "x"),
        map(int),
        map(lambda bus: [
            bus,
            earliest_after(start)(bus),
        ]),
        minimum_by(lambda entry: entry[1]),
        lambda m: m[0] * (m[1] - start)
    ))


assert part_1(test_data) == 295


print(part_1(real_data))


def chinese_remainder_theorem(items):
    """
    copy paste from
    https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
    """
    from functools import reduce

    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1

        if b == 1: return 1

        while a > 1:
            q = a // b
            a, b = b, a%b
            x0, x1 = x1 - q * x0, x0

        if x1 < 0: x1 += b0

        return x1

    def chinese_remainder(n, a):
        sum = 0
        prod = reduce(lambda a, b: a*b, n)

        for n_i, a_i in zip(n, a):
            p = prod // n_i
            sum += a_i * mul_inv(p, n_i) * p

        return sum % prod

    return chinese_remainder(*unzip(items))


def part_2(data):
    busses_with_remainders = apply_to(data[1], compose(
        lambda d: d.split(","),
        enumerate,
        filter_with(lambda item: item[1] != "x"),
        # specify remainders
        map(lambda x: [int(x[1]), -x[0]]),
        list
    ))

    return chinese_remainder_theorem(busses_with_remainders)


assert part_2(test_data) == 1068781


print(part_2(real_data))
