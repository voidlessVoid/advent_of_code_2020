import os
from collections import deque


CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    p1, p2 = [deque([ int(x) for x in pinput.split("\n")[1:]]) for pinput in read_input_text().split("\n\n")]

    while p1 and p2:
        c1, c2 = p1.popleft(), p2.popleft()
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)

    finalList = list(p1 or p2)
    print(sum([finalList[-ix] * ix for ix in range(1, len(finalList) +1)]))

def part_b():

    def play(players):
        states = set()

        while all(players):
            state = (tuple(players[0]), tuple(players[1]))
            if state in states:
                return 0
            states.add(state)

            c1, c2 = [p.popleft() for p in players]
            if c1 <= len(players[0]) and c2 <= len(players[1]):
                winner = play([deque(list(players[0])[:c1]),deque(list(players[1])[:c2])])
            elif c1 > c2:
                winner = 0
            else:
                winner = 1

            if winner:
                players[1].append(c2)
                players[1].append(c1)
            else:
                players[0].append(c1)
                players[0].append(c2)

        if players[0]:
            return 0
        else:
            return 1


    players = [deque([ int(x) for x in pinput.split("\n")[1:]]) for pinput in read_input_text().split("\n\n")]


    play(players)
    finalList = list(players[0] or players[1])
    print(players)
    print(sum([finalList[-ix] * ix for ix in range(1, len(finalList) +1)]))

part_b()
# 5870 too low