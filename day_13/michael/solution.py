import os
import numpy as np

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)


def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]


def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    time, busIntervals = read_input_lines()
    time = int(time)
    busIntervals = [int(x) for x in busIntervals.split(",") if x != "x"]
    idNextDeparture = sorted([(x - (time % x), x) for x in busIntervals])
    print(idNextDeparture[0][0] * idNextDeparture[0][1])


def part_b():
    busIntervals = read_input_lines()[1].split(",")
    constraints = {(offset, int(id)) for offset, id in zip(range(len(busIntervals)), busIntervals) if id != "x"}
    first = constraints.pop()

    currentTime = first[1] - first[0]
    stepsize = first[1]

    while True:
        satisfied_constraints = {x for x in constraints if (currentTime + x[0]) % x[1] == 0}

        if satisfied_constraints:
            for constraint in satisfied_constraints:
                stepsize = np.lcm(stepsize, constraint[1], dtype='int64')
            constraints -= satisfied_constraints

        if not constraints:
            break

        currentTime += stepsize

    print(currentTime)


part_b()

# part_a()
