from functools import reduce

from data import read_lines
from util import filter


get_data = lambda: read_lines(3)

get_data_2 = lambda: [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


ct = lambda gen: len(list(gen))


def every_nth(items, n):
    for index, item in enumerate(items):
        if index % n == 0:
            yield item


def traverse(lines, slope):
    y_vel, x_vel = slope

    for x_pos, line in enumerate(every_nth(lines, x_vel)):
        y_pos = (x_pos * y_vel) % len(line)

        yield [line[y_pos], x_pos, y_pos]


def trees_hit(lines, slope):
    for ground, x_pos, y_pos in traverse(lines, slope):
        if ground is "#":
            yield [x_pos, y_pos]


def slope_qualities(data, slopes):
    for slope in slopes:
        yield ct(trees_hit(data(), slope))


# print(ct(trees_hit(get_data(), (3, 1))))

slopes_to_check = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

print(list(slope_qualities(get_data, slopes_to_check)))

print("mult", reduce(
    lambda x, y: x * y,
    slope_qualities(get_data, slopes_to_check),
    1
))


# for x in traverse(get_data_2(), (1, 2)):
#     print(x)

2655892800
