in_file = "input.txt"

import re
from itertools import groupby, zip_longest


def load_input(file):
    """
    the re.split creates the bug with the input files, the last empty line of the document has in influence, but I don't know why at the moment
    """
    with open(file, 'r') as f:
        in_str = f.read()
    return re.split(r"[\s,\n]", in_str)


def format_passports(in_list):
    pass_list = (list(passport) for _, passport in groupby(in_list, key=''.__ne__))
    return [a + b for a, b in zip(pass_list, pass_list)]


def validate_passport(pass_list):
    val_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    pass_pattern = re.compile(r"(\w{3}):(.*)")
    val1_counter = 0
    passport_dict = {}
    for i, passport in enumerate(pass_list):
        temp_dict = {}
        for line in passport[:-1]:
            temp = pass_pattern.match(line)
            temp_dict[temp.group(1)] = temp.group(2)
        rest = set(val_keys) - set(temp_dict.keys())
        if len(rest) == 0:
            val1_counter += 1
            passport_dict[i] = temp_dict
        elif len(rest) > 0 and "cid" in rest:
            val1_counter += 1
            passport_dict[i] = temp_dict
    val2_counter = 0

    for k, v in passport_dict.items():
        if re.match("^(19[2-8][0-9]|199[0-9]|200[0-2]$)", v["byr"]):
            if re.match("^(201[0-9]|2020)$", v["iyr"]):
                if re.match("^(202[0-9]|2030)$", v["eyr"]):
                    if re.match("(1[5-8][0-9]|19[0-3])cm", v["hgt"]) or re.match("(59|6[0-9]|7[0-6])in", v["hgt"]):
                        if re.match("^#[a-zA-Z0-9]{6}$", v["hcl"]):
                            if v["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                                if re.match("\d{9}", v["pid"]):
                                    val2_counter += 1

    return val1_counter, val2_counter


def puzzle1_2():
    a, b = validate_passport(format_passports(load_input(in_file)))
    print(f"Valid passports by fields: {a} by field values: {b}")


if __name__ == '__main__':
    puzzle1_2()
