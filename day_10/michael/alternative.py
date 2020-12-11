from collections import defaultdict

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]


numbers = [0] + sorted([int(x) for x in read_input_lines()])
numberdict = defaultdict(int)
numberdict[0] = 1

for number in numbers[1:]:
    for origin in {number - x for x in range(1,4)}:
        numberdict[number] += numberdict[origin]

print(numberdict[number])