from itertools import combinations
import yaml
import numpy as np

in_file = "input.yaml"


def load_input(file):
    with open(file, 'rb') as f:
        in_dict = yaml.safe_load(f)
    in_dict = [int(x) for x in in_dict.split(" ")]
    return in_dict


def perm(in_list, r):
    com_list = []
    for n in combinations(in_list, r):
        com_list.append(n)
    return com_list


def result(com_list):
    for n in com_list:
        if sum(n) == 2020:
            print(f"Combination: {n} added: {sum(n)} multiplied: {np.prod(n)}")


def puzzle1():
    puzzle1 = load_input(in_file)
    result(perm((puzzle1), 2))


def puzzle2():
    puzzle2 = load_input(in_file)
    result(perm((puzzle2), 3))


if __name__ == '__main__':
    puzzle1()
    puzzle2()
