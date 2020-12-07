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

    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    def validate(instr):
        fields = {x.split(":")[0] for x in instr.split()}
        return not (required - fields)

    records = read_input_text().split("\n\n")
    print(sum([validate(x) for x in records]))


def part_b():

    def validateHeight(fieldValue):
        unit2limits = {"cm": (150,193), "in": (59, 76)}
        match = re.match(r"^(\d+)([a-z]+)$",fieldValue)
        if match and match.group(2) in unit2limits:
            limits = unit2limits[match.group(2)]
            return limits[0] <= int(match.group(1)) <= limits[1]


    validations = {
        "byr": lambda x: (len(x) == 4) and ("1920" <= x <= "2002"),
        "iyr": lambda x: (len(x) == 4) and ("2010" <= x <= "2020"),
        "eyr": lambda x: (len(x) == 4) and ("2020" <= x <= "2030"),
        "hgt": lambda x: bool(validateHeight(x)),
        "hcl": lambda x: bool(re.match(r"^#[0-9a-f]{6}$", x)),
        "ecl": lambda x: x in ("amb blu brn gry grn hzl oth".split()),
        "pid": lambda x: (len(x) == 9) and x.isdigit() }

    def validate(instr):
        fieldtoValueDict = {field: value for field, value in [x.split(":") for x in instr.split()] }
        return all(((field in fieldtoValueDict) and test(fieldtoValueDict[field]) for field, test in validations.items()))

    records = read_input_text().split("\n\n")
    print(sum([validate(x) for x in records]))

part_a()
part_b()


