import re

in_file = "input.txt"


def read_input_lines():
    with open(in_file, 'r') as f:
        return [x.strip() for x in f.readlines()]


def section(strfrac, pattern):
    pattern = re.compile(pattern)
    seq = re.search(pattern, strfrac)
    while seq:
        value = eval(seq.group())
        strfrac = strfrac[:seq.span()[0]] + str(value) + strfrac[seq.span()[1]:]
        seq = re.search(pattern, strfrac)
    return strfrac


def stepwise(strfrac, pattern):
    pattern = re.compile(pattern)
    seq = re.search(pattern, strfrac)
    while seq:
        value = eval(seq.group())
        strfrac = str(value) + strfrac[seq.span()[1]:]
        seq = re.search(pattern, strfrac)
    return strfrac


def elf_math(strfrac):
    return section(strfrac, r"(\d+) \+ (\d+)|(\d+) \* (\d+)")


def advanced_elf_math(strfrac):
    strfrac = section(strfrac, r"(\d+) [+] (\d+)")
    strfrac = stepwise(strfrac, r"(\d+) [*] (\d+)")
    return strfrac


def puzzle1():
    data = read_input_lines()
    total_sum = 0
    for line in data:
        # evaluate bracketed expressions
        if "(" in line:
            pattern = re.compile(r"\([\d+ [+*]*]*\)")
            seq = re.search(pattern, line)
            while seq:
                value = elf_math(seq.group()[1:-1])
                line = line[:seq.span()[0]] + str(value) + line[seq.span()[1]:]
                seq = re.search(pattern, line)
        # evaluate te residuum string
        line = elf_math(line)
        total_sum += int(line)
    print(f"Total sum of elf on a shelf math: {total_sum}")


def puzzle2():
    data = read_input_lines()
    total_sum = 0
    for line in data:
        # evaluate bracketed expressions
        if "(" in line:
            pattern = re.compile(r"\([\d+ [+*]*]*\)")
            seq = re.search(pattern, line)
            while seq:
                value = advanced_elf_math(seq.group()[1:-1])
                line = line[:seq.span()[0]] + str(value) + line[seq.span()[1]:]
                seq = re.search(pattern, line)
        # evaluate te residuum string
        line = advanced_elf_math(line)
        total_sum += int(line)
    print(f"Total sum of advanced elf on a shelf math: {total_sum}")


if __name__ == '__main__':
    puzzle1()
    puzzle2()
