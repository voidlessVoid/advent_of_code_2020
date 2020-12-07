import re

in_file = "input.txt"


def read_input_lines():
    with open(in_file, 'r') as fh:
        return [x.strip() for x in fh.readlines()]


prefix_pattern = re.compile(rf"^([a-z]* [a-z]*) bags")
color_pattern = re.compile(rf"(\d) ([a-z]* [a-z]*) (?:bag|bags)")


def color_rules(in_list):
    rule_dict = {}
    for value in in_list:
        temp_dict = {}
        index = re.match(prefix_pattern, value)
        colors = re.findall(color_pattern, value)
        for color in colors:
            temp_dict[color[1]] = color[0]
        rule_dict[index.group(1)] = temp_dict
    return rule_dict


def puzzle1():
    rule_dict = color_rules(read_input_lines())
    color_list = ['shiny gold']

    def __color_update(in_color_list):
        color_list = []
        for color in in_color_list:
            for k, v in rule_dict.items():
                if color in v.keys():
                    color_list.append(k)
        return list(set(color_list))

    color_counter_list = []
    while color_list:
        color_list = __color_update(color_list)
        color_counter_list += color_list

    print(f"Number of bag colors: {len(set(color_counter_list))}")


def puzzle2():
    rule_dict = color_rules(read_input_lines())
    bags = [("shiny gold", 1, 1)]

    def __packing_map(bags_tuple_list):
        bags_old = bags_tuple_list.copy()
        bags_tuple_list = []
        for bag_color in bags_old:
            if bags_old:
                for k, v in rule_dict[bag_color[0]].items():
                    bags_tuple_list.append((k, int(v), bag_color[2] * int(v)))
        return bags_tuple_list

    bags_new = bags.copy()
    while bags_new:
        bags_new = __packing_map(bags_new)
        bags += bags_new

    counter = -1
    for bag in bags:
        counter += bag[2]

    print(f"Total number of bags: {counter}")


if __name__ == '__main__':
    puzzle1()
    puzzle2()
