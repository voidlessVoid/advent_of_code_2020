import re
from itertools import product

in_file = "input.txt"


def read_input_lines():
    with open(in_file, 'r') as fh:
        in_string = fh.read().replace("\n", " ")
    return in_string.split("mask = ")[1:]


def format_input():
    data = read_input_lines()
    pattern = re.compile("mem\[(\d+)\] = (\d+)")
    data_list = []
    for line in data:
        addresses = re.findall(pattern, line)
        data_list.append([line[:36]] + addresses)
    return data_list


def intstr_to_bin(value):
    return f"{int(value):b}"


def puzzle1():
    data = format_input()
    memory = {}
    for n in data:
        mask = n[0]
        mask_ind = [(i, v) for i, v in enumerate(mask) if v != "X"]
        for address in n[1:]:
            value = intstr_to_bin(address[1])
            value36 = value.rjust(36, "0")
            for m in mask_ind:
                value36 = value36[:m[0]] + m[1] + value36[m[0] + 1:]
            memory[address[0]] = value36
    result = sum([int(value, 2) for value in memory.values()])
    print(f"Sum of memory values: {result}")


def puzzle2():
    data = format_input()
    memory_register = {}
    for n in data:
        mask = n[0]
        mask_ind = [(i, v) for i, v in enumerate(mask) if v != "0"]
        for address in n[1:]:
            value = intstr_to_bin(address[0])
            value36 = value.rjust(36, "0")

            x_list = product(["0", "1"], repeat=len([x[1] for x in mask_ind if x[1] == "X"]))
            x_add = [x[0] for x in mask_ind if x[1] == "X"]
            x_replace = []
            for x in x_list:
                x_replace.append(list(zip(x_add, x)))

            for m in mask_ind:
                value36 = value36[:m[0]] + m[1] + value36[m[0] + 1:]
            for x_set in x_replace:
                for char in x_set:
                    value36 = value36[:char[0]] + char[1] + value36[char[0] + 1:]
                memory_register[value36] = address[1]
    result = sum([int(value) for value in memory_register.values()])
    print(f"Sum of memory values: {result}")


if __name__ == '__main__':
    puzzle1()
    puzzle2()
