class input_handler():
    def __init__(self):
        self.in_file = "input.txt"

    def load_input(self):
        with open(self.in_file, 'r') as f:
            in_list = [line.rstrip('\n') for line in f]
        return in_list


class TobogganTrajectory:
    def __init__(self, movement):
        self.map_pattern = input_handler().load_input()
        self.movement = movement
        self.Map = self.multiply_pattern()
        self.tree_counter = 0

    def multiply_pattern(self):
        while len(self.map_pattern[0]) < len(self.map_pattern) * self.movement[1]:
            for i, line in enumerate(self.map_pattern.copy()):
                self.map_pattern[i] = line * 2
        return self.map_pattern

    def show_map(self):
        for line in self.Map:
            print(line)
        return self.Map

    def naviagte(self):
        pos = [0, 0]
        # tree_counter = 0
        while pos[0] != len(self.Map):
            try:
                # replace map value
                if self.Map[pos[0]][pos[1]] == ".":
                    sym = "O"  # empty field
                else:
                    sym = "X"  # Tree
                    self.tree_counter += 1
            except IndexError:
                break
            self.Map[pos[0]] = self.Map[pos[0]][:pos[1]] + sym + self.Map[pos[0]][pos[1] + 1:]
            # new position
            pos = [pos[i] + self.movement[i] for i in range(len(pos))]


def puzzle1():
    Route = TobogganTrajectory(movement=[1, 3])
    Route.naviagte()
    Route.show_map()
    print(f"Total number of trees: {Route.tree_counter}")


def puzzle2():
    from itertools import accumulate
    slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
    tree_list = []
    for slope in slopes:
        Route = TobogganTrajectory(movement=slope)
        Route.naviagte()
        tree_list.append(Route.tree_counter)
    tree_prod = [*accumulate(tree_list, lambda a, b: a * b)]

    print(f"Multiplied number of trees: {tree_prod[-1]}")


if __name__ == '__main__':
    # show_map(multiply_pattern(load_input(in_file)))
    puzzle1()
    puzzle2()
