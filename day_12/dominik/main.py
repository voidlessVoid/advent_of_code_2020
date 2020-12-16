from itertools import product
import re

in_file = "input.txt"


def read_input_lines():
    with open(in_file, 'r') as fh:
        return [x.strip() for x in fh.readlines()]


def direction_vector(naviagtion_list):
    vector_list = []
    for vector in naviagtion_list:
        pattern = re.compile("^([A-Z])(\d+)$")
        vector = re.match(pattern, vector)
        vector_list.append((vector.group(1), int(vector.group(2))))
    return vector_list


class drunken_sailor:
    def __init__(self, pos, facing, vector):
        self.pos = pos
        self.facing = facing
        self.vector = vector
        self.nav_dict = {
            "N": self.__north,
            "E": self.__east,
            "S": self.__south,
            "W": self.__west,
            "F": self.__forward,
            "R": self.__rotate,
            "L": self.__rotate
            }
        self.nav_dict[self.vector[0]]()

    def __north(self):
        self.pos[1] += self.vector[1]

    def __south(self):
        self.pos[1] -= self.vector[1]

    def __east(self):
        self.pos[0] += self.vector[1]

    def __west(self):
        self.pos[0] -= self.vector[1]

    def __forward(self):
        self.nav_dict[self.facing]()

    def __rotate(self):
        d = {
            "N": 0,
            "E": 90,
            "S": 180,
            "W": 270
            }
        if self.vector[0] in ["R", "L"]:
            if self.vector[0] == "R":
                v = d[self.facing] + self.vector[1]
            else:
                v = d[self.facing] - self.vector[1]
            if v >= 360:
                v -= 360
            if v < 0:
                v += 360
            for key, value in d.items():
                if v == value:
                    self.facing = key


class navigate_corretly:
    def __init__(self, wp, pos, vector):
        self.wp = wp
        self.pos = pos
        self.vector = vector
        self.nav_dict = {
            "N": self.__north,
            "E": self.__east,
            "S": self.__south,
            "W": self.__west,
            "F": self.__forward,
            "R": self.__rotate,
            "L": self.__rotate
            }
        self.nav_dict[self.vector[0]]()

    def __north(self):
        self.wp[1] += self.vector[1]

    def __south(self):
        self.wp[1] -= self.vector[1]

    def __east(self):
        self.wp[0] += self.vector[1]

    def __west(self):
        self.wp[0] -= self.vector[1]

    def __forward(self):
        self.pos[0] += self.wp[0] * self.vector[1]
        self.pos[1] += self.wp[1] * self.vector[1]

    def __rotate(self):
        times = self.vector[1] // 90
        if self.vector[0] in ["R", "L"]:
            if self.vector[0] == "R":
                for x in range(times):
                    self.wp = [self.wp[1], -1 * self.wp[0]]
            else:
                for x in range(times):
                    self.wp = [-1 * self.wp[1], self.wp[0]]


def puzzle1():
    in_data = read_input_lines()
    navigation_map = direction_vector(in_data)
    pos = [0, 0]
    facing = "E"
    for step in navigation_map:
        Ship = drunken_sailor(pos=pos, facing=facing, vector=step)
        pos = Ship.pos
        facing = Ship.facing
    print(f"Manhatten Distance: {abs(pos[0]) + abs(pos[1])}")


def puzzle2():
    in_data = read_input_lines()
    navigation_map = direction_vector(in_data)
    waypoint = [10, 1]
    pos = [0, 0]

    for step in navigation_map:
        Ship = navigate_corretly(pos=pos, wp=waypoint, vector=step)
        pos = Ship.pos
        waypoint = Ship.wp
    print(f"Manhatten Distance: {abs(pos[0]) + abs(pos[1])}")


if __name__ == '__main__':
    test = puzzle1()
    puzzle2()
