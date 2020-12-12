import os

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)


def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]


def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    instructions = read_input_lines()
    dirs = (1, -1j, -1, 1j)
    sym2dir = dict(zip("ESWN", dirs))

    loc = 0
    dirix = 0
    for instruction in instructions:
        if instruction.startswith("F"):
            loc += (dirs[dirix] * int(instruction[1:]))
        elif instruction.startswith("R"):
            dirix = (dirix + (int(instruction[1:]) // 90)) % 4
        elif instruction.startswith("L"):
            dirix = (dirix - (int(instruction[1:]) // 90)) % 4
        else:
            loc += sym2dir[instruction[0]] * int(instruction[1:])

    print(abs(loc.real) + abs(loc.imag))


def part_b():
    instructions = read_input_lines()
    dirs = (1, -1j, -1, 1j)
    sym2dir = dict(zip("ESWN", dirs))
    turnRight = lambda w: w.imag - (1j * w.real)

    locWaypoint = 10 + 1j
    loc = 0
    for instruction in instructions:
        if instruction.startswith("F"):
            loc += (locWaypoint) * int(instruction[1:])
        elif instruction.startswith("R"):
            for rightTurns in range((int(instruction[1:]) // 90) % 4):
                locWaypoint = turnRight(locWaypoint)
        elif instruction.startswith("L"):
            for rightTurns in range((-(int(instruction[1:]) // 90)) % 4):
                locWaypoint = turnRight(locWaypoint)
        else:
            locWaypoint += sym2dir[instruction[0]] * int(instruction[1:])

    print(abs(loc.real) + abs(loc.imag))


part_a()
part_b()
