import re

in_file = "input.txt"

pw_pattern = re.compile("(\d*)-(\d*) (\w): ([a-z]*)")

def load_input(file):
    with open(file, 'r') as f:
        in_list = [line.rstrip('\n') for line in f]
    return in_list


def validate_pass1(in_list):
    counter = 0
    for value in in_list:
        policy = pw_pattern.search(value)
        pw = policy.group(4)
        validate_count = pw.count(policy.group(3))
        if validate_count >= int(policy.group(1)) and validate_count <= int(policy.group(2)):
            counter += 1
    return counter


def validate_pass2(in_list):
    counter = 0
    for value in in_list:
        policy = pw_pattern.search(value)
        case1 = re.search((re.compile(rf'^.{{{int(policy.group(1)) - 1}}}[{policy.group(3)}]')), policy.group(4))
        case2 = re.search((re.compile(rf"^.{{{int(policy.group(2)) - 1}}}[{policy.group(3)}]")), policy.group(4))

        if case1 and case2 is None:
            counter += 1
        elif case1 is None and case2:
            counter += 1

    return counter


def puzzle1():
    in_data = load_input(in_file)
    count = validate_pass1(in_data)
    print(f"Puzzle1: Total number of valid PW: {count}")


def puzzle2():
    in_data = load_input(in_file)
    count = validate_pass2(in_data)
    print(f"Puzzle2: Total number of valid PW: {count}")


if __name__ == '__main__':
    puzzle1()
    puzzle2()
