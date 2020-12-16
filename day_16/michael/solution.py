import os
import re
import operator
from functools import reduce

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)


def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]


def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def rule2set(instr):
    ranges = re.findall("\d+\-\d+", instr)
    ranges = [[int(y) for y in x.split("-")] for x in ranges]
    valid = reduce(operator.or_, [set(range(x[0], x[1] + 1)) for x in ranges])
    return valid


def part_a():
    rules, myTicket, otherTickets = read_input_text().split("\n\n")
    valid = rule2set(rules)

    otherTicketNumbers = [int(x) for x in re.findall("\d+", otherTickets)]
    print(sum(x for x in otherTicketNumbers if x not in valid))


def part_b():
    rules, myTicket, otherTickets = read_input_text().split("\n\n")
    nRules = len(rules.split("\n"))

    rule2valid = {k: rule2set(v) for k, v in [x.split(":") for x in rules.split("\n")]}
    allvalid = rule2set(rules)

    otherTickets = [[int(y) for y in x.split(",")] for x in otherTickets.split("\n")[1:]]
    otherTicketsFilterd = [x for x in otherTickets if not (set(x) - allvalid)]

    column2numbers = {i: {x[i] for x in otherTicketsFilterd} for i in range(nRules)}
    column2rule = {i: {r for r, valid in rule2valid.items() if not (numbers - valid)} for i, numbers in
                   column2numbers.items()}

    solved = {}
    while len(solved) < nRules:

        for i, v in list(column2rule.items()):
            if len(v) == 1:  # 1 option for column
                solved[v.pop()] = i
                del column2rule[i]

        for ruleName in rule2valid:
            validColumns = {ix for ix, validRules in column2rule.items() if ruleName in validRules}
            if len(validColumns) == 1:  # 1 option for a rule
                column = validColumns.pop()
                solved[ruleName] = column
                del column2rule[column]

    myTicket = [int(x) for x in re.findall("\d+", myTicket)]
    print(reduce(operator.mul, [myTicket[ix] for ruleName, ix in solved.items() if ruleName.startswith("departure")]))


part_a()
part_b()
