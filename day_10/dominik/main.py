from copy import deepcopy

in_file = "input.txt"


def read_input_lines():
    with open(in_file, 'r') as fh:
        return [int(x.strip()) for x in fh.readlines()]


def puzzle1():
    lower = read_input_lines()
    lower.append(0)
    upper = read_input_lines()
    upper.append(max(upper) + 3)

    lower = set(lower)
    upper = set(upper)

    diffs = []

    for i, n in zip(lower, upper):
        diffs.append(n - i)

    print(f"Number of 1jolt diff: {diffs.count(1)}, Number of 3jolt diff: {diffs.count(3)}, Result: {diffs.count(1) * diffs.count(3)}")


def puzzle2():
    data = read_input_lines()
    data.append(0)
    data.append(max(data) + 3)
    data.sort()
    solutions = []

    def __rangetest(upper, lower):
        diffs = []
        for i, n in zip(lower, upper):
            diffs.append(n - i)
        if all(n == 1 or n == 3 for n in diffs):
            print("valid solution", set(lower + upper))
            solutions.append(set(lower + upper))
        else:
            return False

    n = -1
    while -n < len(data):
        lower = deepcopy(data)[:n]
        upper = deepcopy(lower)[1:]
        upper.append(max(data))
        print(set(lower + upper))
        # __rangetest(upper,lower)
        n -= 1
        print(solutions)


if __name__ == '__main__':
    puzzle1()
    puzzle2()
