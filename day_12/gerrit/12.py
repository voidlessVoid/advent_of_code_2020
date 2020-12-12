import numpy as np

from data import read_lines


real_data = list(read_lines(12))


test_data = [
    "F10",
    "N3",
    "F7",
    "R90",
    "F11",
]


directions = ["N", "E", "S", "W"]


def instructions(raw_instructions):
    for instr in raw_instructions:
        yield [instr[0], int(instr[1:])]


def part_1(data):
    position = [0, 0]

    direction = "E"

    for d, v in instructions(data):
        if d in ["L", "R"]:
            current = directions.index(direction)
            turns = v / 90
            sign = 1 if d == "R" else -1

            direction = directions[int(current + sign * turns) % len(directions)]
        else:
            dir_to_move = direction if d == "F" else d

            sign = 1 if dir_to_move in ["S", "E"] else -1

            position = [
                position[0] if dir_to_move in ["E", "W"] else position[0] + sign * v,
                position[1] if dir_to_move in ["N", "S"] else position[1] + sign * v,
            ]

    return abs(position[0]) + abs(position[1])


assert part_1(test_data) == 25


print(part_1(real_data))


def rotate(vec, turns):
    mats = {
        0: [[ 1,  0], [ 0,  1]],
        1: [[ 0, -1], [ 1,  0]],
        2: [[-1,  0], [ 0, -1]],
        3: [[ 0,  1], [-1,  0]],
    }

    mat = np.array(mats[turns % 4])

    return list(mat.dot(np.array(vec)).astype(int))


def part_2(data):
    position = [0, 0]
    velocity = [1, 10]

    for i, n in instructions(data):
        if i == "F":
            position = [
                position[0] + n * velocity[0],
                position[1] + n * velocity[1],
            ]
        elif i in ["L", "R"]:
            sign = 1 if i == "R" else -1
            turns = int(sign * n / 90)
            velocity = rotate(velocity, turns)
        else:
            sign = 1 if i in ["N", "E"] else -1

            delta = [
                sign * n if i in ["N", "S"] else 0,
                0        if i in ["N", "S"] else sign * n,
            ]

            velocity = [
                velocity[0] + delta[0],
                velocity[1] + delta[1],
            ]

    return abs(position[0]) + abs(position[1])


assert part_2(test_data) == 286


print(part_2(real_data))


assert part_2(real_data) == 52742
