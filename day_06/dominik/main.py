from itertools import groupby

in_file = "input.txt"


def load_input(file):
    with open(file, 'r') as f:
        in_list = [line.rstrip('\n') for line in f]
        in_list.append("")  # at has to be an even number of lines, otherwise the zip command deletes the last row
        grouped_list = (list(entry) for _, entry in groupby(in_list, key=''.__ne__))
        list_of_lists = [a + b for a, b in zip(grouped_list, grouped_list)]
    return list_of_lists


def puzzle1():
    data = load_input(in_file)
    data = ["".join(n) for n in data]
    counter = 0
    for n in data:
        counter += len(set(n))
    print(f"Sum of Counts: {counter}")
    return data, counter


def puzzle2():
    data = load_input(in_file)
    counter = 0
    for n in data:
        ns = n[:-1]
        print(ns)
        if len(ns) == 1:
            counter += len(ns[0])
        else:
            keys = set("".join(ns))
            values = [0 for x in range(len(keys))]
            counter_dict = dict(zip(keys, values))
            for person in ns:
                for char in person:
                    counter_dict[char] += 1
            for v in counter_dict.values():
                if v == len(ns):
                    counter += 1
    print(f"Sum of correct counts: {counter}")
    return data, counter


if __name__ == '__main__':
    a = puzzle1()
    b = puzzle2()
