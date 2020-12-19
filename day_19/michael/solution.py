import os
from functools import reduce

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()



def solve(rule, input, ix, rules,visited):
    """ returns valid index continues to continue after this match. If not match it returns empty set"""
    solutions = set()
    if ((rule, ix) in visited) or ix == len(input):
        return solutions

    for char in "ab":
        if char in rule:
            if char == input[ix]:
                solutions.add(ix+1)
            return solutions

    ruleOptions = rule.split("|")

    for ruleOption in ruleOptions:
        ruleNumbers = ruleOption.split()
        currentixes = {ix}

        for ruleNumber in ruleNumbers:
            currentixes = reduce(lambda x,y : x|y,  [solve(rules[ruleNumber],input,i,rules, visited | {(rule,ix)}) for i in currentixes])
            if not currentixes:
                break
        else:
            solutions |= currentixes

    return solutions


def part_a():

    def validate(line):
        solutions = solve(rules["0"], line, 0, rules, set())
        return len(line) in solutions

    rules, text = [x.split("\n") for x in read_input_text().split("\n\n")]
    rules = {x.split(":")[0]:x.split(":")[1] for x in rules}

    print(len([l for l in text if validate(l)]))


def part_b():

    def validate(line):
        solutions = solve(rules["0"], line, 0, rules, set())
        return len(line) in solutions

    rules, text = [x.split("\n") for x in read_input_text().split("\n\n")]
    rules = {x.split(":")[0]:x.split(":")[1] for x in rules}
    rules["8"] =  "42 | 42 8"
    rules["11"] = "42 31 | 42 11 31"

    print(len([l for l in text if validate(l)]))

part_a()
part_b()
