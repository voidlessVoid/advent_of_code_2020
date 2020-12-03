from itertools import accumulate

in_file = "input.txt"

def load_input(file):
    with open(file, 'r') as f:
        in_list = [line.rstrip('\n') for line in f]
    return in_list


def multiply_pattern(pattern_list, movement):
    while len(pattern_list[0]) < len(pattern_list) * movement[1]:
        for i, line in enumerate(pattern_list.copy()):
            pattern_list[i] = line * 2
    return pattern_list


def show_map(Map):
    for line in Map:
        print(line)
    return Map


def naviagte(movement):
    map_pattern = load_input(in_file)
    Map = multiply_pattern(map_pattern, movement)
    pos = [0, 0]
    tree_counter = 0
    while pos[0] != len(Map):
        try:
            # replace map value
            if Map[pos[0]][pos[1]] == ".":
                sym = "O"  # empty field
            else:
                sym = "X"  # Tree
                tree_counter += 1
        except IndexError:
            break
        Map[pos[0]] = Map[pos[0]][:pos[1]] + sym + Map[pos[0]][pos[1] + 1:]
        # new position
        pos = [pos[i] + movement[i] for i in range(len(pos))]
    return Map, tree_counter


def puzzle1():
    Map, tree = naviagte([1, 3])
    show_map(Map)
    print(f"Total number of trees: {tree}")

def puzzle2():
    slopes=[[1,1],[1,3],[1,5],[1,7],[2,1]]
    tree_list=[]
    for slope in slopes:
        Map, tree = naviagte(slope)
        tree_list.append(tree)
    tree_prod=[*accumulate(tree_list, lambda a, b: a*b)]

    print(f"Multiplied number of trees: {tree_prod[-1]}")

if __name__ == '__main__':
    # show_map(multiply_pattern(load_input(in_file)))
    puzzle1()
    puzzle2()

