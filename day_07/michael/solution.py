import os
from collections import defaultdict


CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

def parseInnerBag(bag):
    words = [ w for w in bag.split(" ") if w]
    return int(words[0]), " ".join(words[1:3])


def parseLines(lines):
    bag2content = {}
    content2parents = defaultdict(list)
    for line in lines:
        outer, inner = line.split("contain")
        outer = " ".join(outer.split(" ")[:2])
        if inner.endswith("no other bags."):
            bag2content[outer] = []
        else:
            bag2content[outer] = [parseInnerBag(x) for x in inner.split(",")]
            for innerBag in bag2content[outer]:
                content2parents[innerBag[1]].append(outer)

    return bag2content, content2parents

def part_a():

    def solve(currentBag, content2parents):
        return set(content2parents[currentBag]).union(*[solve(x, content2parents) for x in content2parents[currentBag]])

    lines = read_input_lines()
    _, content2parents = parseLines(lines)
    print(len(solve("shiny gold", content2parents)))


def part_b():

    def solve(currentBag, bag2content):
        return sum([solve(bag,bag2content) * number + number for number, bag in bag2content[currentBag]])

    lines = read_input_lines()
    bag2content, _ = parseLines(lines)
    print(solve("shiny gold", bag2content))

part_a()
part_b()