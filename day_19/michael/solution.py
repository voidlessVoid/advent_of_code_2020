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
    def evalstring(instr,ix):

        running = None
        operator = None
        val = None
        while ix < len(instr):
            if instr[ix].isdigit():
                val = int(instr[ix])
            elif instr[ix] == "(":
                val, ix = evalstring(instr,ix+1)
            elif instr[ix] in "+*":
                operator = instr[ix]

            elif instr[ix] == ")":
                return [running, ix]

            if val:
                if running is None:
                    running= int(val)
                else:
                    running  = eval(f"{running} {operator} {val}")
                    operator = None

            val = None
            ix+=1
        return running

    print(sum([evalstring(x,0) for x in read_input_lines()]))


def part_b():
    def evalstring(instr, ix):

        parseTokens = []

        while ix < len(instr):
            if instr[ix].isdigit():
                parseTokens.append(int(instr[ix]))
            elif instr[ix] == "(":
                val, ix = evalstring(instr, ix + 1) #we evaluate the bracket section and val goes on the tokenlist
                parseTokens.append(val)
            elif instr[ix] in "+*":
                parseTokens.append(instr[ix])

            elif instr[ix] == ")":
                break
            ix += 1

        # first handle all the + operations. Afterwards we can just eval the rest in a straightforward way
        parseRight = deque(parseTokens)
        parseLeft = deque([])

        while parseRight:
            token = parseRight.popleft()
            if token == "+":
                v1 = parseLeft.pop()
                v2 = parseRight.popleft()
                token = v1 + v2

            parseLeft.append(token)

        result = eval("".join([str(x) for x in parseLeft]))
        return result, ix

    print(sum([evalstring(x,0)[0] for x in read_input_lines()]))

part_b()



