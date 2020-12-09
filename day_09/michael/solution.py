import os

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    def indexValid(i):
        distinctPrevious = set(numbers[i-25:i])
        return {(x+y) for x in distinctPrevious for y in distinctPrevious if (x+y == numbers[i]) and (x!= y)}

    numbers = [int(i) for i in read_input_lines()]
    print(numbers[next((i for i in range(25,len(numbers)) if not indexValid(i)))])


def part_b():
    answer = 133015568
    numbers = [int(i) for i in read_input_lines()]
    validrange = next((numbers[a:b] for a in range(len(numbers)-1) for b in range(a+2,len(numbers)) if sum(numbers[a:b]) == answer))
    print(min(validrange) + max(validrange))

part_a()
part_b()