import os

from collections import Counter, ChainMap, defaultdict, deque


CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    input = list("469217538")
    sortedInput = sorted(input)
    minus1map = {sortedInput[ix]:sortedInput[ix-1] for ix in range(len(sortedInput))}

    for step in range(100):
        current = input[0]
        pickUp = input[1:4]
        destination = minus1map[current]
        while destination in pickUp:
            destination = minus1map[destination]


        input = input[4:] + [current]
        destinationix = input.index(destination)
        input = input[:destinationix+1] + pickUp + input[destinationix+1:]

    index1 = input.index('1')
    print("".join(input[index1+1:] + input[:index1]))

part_a()

def part_b():

    input = "469217538"
    nextNode = {int(input[i]): int(input[(i+1)]) for i in range(8)}
    nextNode[8] = 10
    for i in range(10,10**6):
        nextNode[i] = i+1
    nextNode[10**6] = 4

    current = 4
    for _ in range(10**7):
        pickUpA = nextNode[current]
        pickUpB = nextNode[pickUpA]
        pickUpC = nextNode[pickUpB]
        nextCurrent = nextNode[pickUpC]

        target = ((current - 2) % 10**6) +1
        while target in [pickUpA,pickUpB,pickUpC]:
            target = ((target - 2) % 10 ** 6) + 1

        targetPerviousNextNode = nextNode[target]
        nextNode[current] = nextCurrent # skip the 3
        nextNode[target] = pickUpA
        nextNode[pickUpC] = targetPerviousNextNode

        current = nextCurrent


    nextTo1 = nextNode[1]
    nextNextTo1 = nextNode[nextTo1]

    print( nextTo1 * nextNextTo1)

part_b()

