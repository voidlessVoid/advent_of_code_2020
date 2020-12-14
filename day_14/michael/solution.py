import os
import re

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)


def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]


def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    registers = {}
    for line in read_input_lines():
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
        else:
            key, value = [int(x) for x in re.findall(r"\d+", line)]
            value = (str(bin(value))[2:]).zfill(36)
            value = sum([int(mask[ix].replace("X", value[ix])) * (2 ** (35 - ix)) for ix in list(range(36))])
            registers[key] = value

    print(sum(registers.values()))


def part_b():
    def getAll(maskString, keyString):
        values = {0}
        for ix in range(36):
            if maskString[ix] == "X":
                values |= {x + (2 ** (35 - ix)) for x in values}
            elif (maskString[ix] == "1") or (keyString[ix] == "1"):
                values = {x + (2 ** (35 - ix)) for x in values}

        return values

    registers = {}
    for line in read_input_lines():
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
        else:
            key, value = [int(x) for x in re.findall(r"\d+", line)]
            key = (str(bin(key))[2:]).zfill(36)
            keys = getAll(mask, key)
            for key in keys:
                registers[key] = value

    print(sum(registers.values()))


part_a()
part_b()
