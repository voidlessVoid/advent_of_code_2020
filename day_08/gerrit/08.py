from util import apply_to, compose

from data import read_lines


real_data = list(read_lines(8))


test_data = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6",
]


def read_program(code):
    for line in code:
        yield line.split(" ")


def run_with(init, step):
    def runner(program):
        instructions = list(program)

        ctx = init
        lines_interpreted = []

        while True:
            pos = ctx["pos"]

            if pos in lines_interpreted or pos == len(instructions):
                break

            command, value = instructions[pos]
            ctx = step[command](int(value))(**ctx)
            lines_interpreted.append(pos)

        return ctx

    return runner


interpreter = {
    "init": {
        "pos": 0,
        "state": 0
    },
    "step": {
        "jmp": lambda value: lambda pos, state: {
            "pos": pos + value,
            "state": state
        },
        "acc": lambda value: lambda pos, state: {
            "pos": pos + 1,
            "state": state + value
        },
        "nop": lambda value: lambda pos, state: {
            "pos": pos + 1,
            "state": state
        }
    }
}


def part_1(data):
    return apply_to(data, compose(
        read_program,
        run_with(**interpreter),
        lambda ctx: ctx["state"]
    ))


def alter_program(program, i):
    command_mapping = {
        "nop": "jmp",
        "jmp": "nop"
    }

    for index, line in enumerate(program):
        command, value = line
        if index == i:
            yield [
                command_mapping.get(command, command),
                value
            ]
        else:
            yield line


def part_2(data):
    original_program = list(read_program(data))

    for i in range(len(original_program)):

        ctx = run_with(**interpreter)(
            alter_program(original_program, i)
        )

        if ctx["pos"] == len(original_program):
            return ctx["state"]


    raise Error("no modification fixed the program")


assert part_1(test_data) == 5
assert part_1(real_data) == 1262

print(part_1(real_data))

assert part_2(test_data) == 8
assert part_2(real_data) == 1643

print(part_2(real_data))

