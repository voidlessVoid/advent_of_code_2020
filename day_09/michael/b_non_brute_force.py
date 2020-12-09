import os

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def part_b():
    answer = 133015568
    numbers = [int(i) for i in read_input_lines()]

    fromIx, toIx = 0, 1 #to is inclusive
    s = sum(numbers[:2])
    while True:
        if s == answer:
            print(min(numbers[fromIx:toIx+1]) + max(numbers[fromIx:toIx+1]))
            break
        elif (s < answer) or ((toIx - fromIx) < 2):
            toIx +=1
            s += numbers[toIx]
        else:
            s -=numbers[fromIx]
            fromIx += 1

part_b()
