from parsec import *

from functools import reduce

from data import read_lines
from util import prod


real_data = list(read_lines(18))


# Parsing

whitespace = regex(r"\s*")

lexeme = lambda p: p << whitespace

lparen = lexeme(string("("))
rparen = lexeme(string(")"))
plus   = lexeme(string("+"))
mult   = lexeme(string("*"))
number = lexeme(regex(r"\d+").parsecmap(int))

op = plus | mult

# ------------------------------------
# Part 1


print("Part 1\n\n")


@generate
def paren_block():
    yield lparen
    expr = yield expression
    yield rparen

    return expr


@generate
def terms():
    first = yield value
    operations = yield many(op + value)

    return reduce(
        lambda acc, step: (
            eval(f"{acc} {step[0]} {step[1]}")
        ),
        operations,
        first
    )


value = number | paren_block
expression = terms ^ value


def evaluate_1(line):
    return expression.parse(line)


# Tests


test_cases_1 = [
    [4, "2 * (1 + 1)"],
    [6, "2 * 3"],
    [26, "2 * 3 + 20"],
    [26, "2 * 3 + (4 * 5)"],
    [437, "5 + (8 * 3 + 9 + 3 * 4 * 3)"],
    [12240, "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"],
    [13632, "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]
]

for expected, expr in test_cases_1:
    result = evaluate_1(expr)
    assert result == expected, f"\t{result} != {expected} in '{expr}'"


# Ouput


def part_1(data):
    return sum(
        evaluate_1(line)
        for line in data
    )


print(part_1(real_data))


# Part 2


print("Part 2\n\n")


@generate
def paren_block_2():
    yield lparen
    expr = yield expression_2
    yield rparen

    return expr


@generate
def addition():
    terms = yield sepBy1(value_2, plus)

    return sum(terms)


@generate
def multiplication():
    terms = yield sepBy1(addition ^ value_2, mult)

    return prod(terms)


value_2 = paren_block_2 | number

expression_2 = (
    multiplication
    ^ addition
    ^ value_2
)


def evaluate_2(line):
    return expression_2.parse(line)


# Tests part 2


test_cases_2 = [
    [4, "2 * (1 + 1)"],
    [51, "1 + (2 * 3) + (4 * (5 + 6))"],
    [46, "2 * 3 + (4 * 5)"],
    [1445, "5 + (8 * 3 + 9 + 3 * 4 * 3)"],
    [669060, "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"],
    [23340, "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]
]


for expected, expr in test_cases_2:
    result = evaluate_2(expr)
    assert result == expected, f"\t{result} != {expected} in '{expr}'"


def part_2(data):
    return sum(
        evaluate_2(line)
        for line in data
    )


print(part_2(real_data))
