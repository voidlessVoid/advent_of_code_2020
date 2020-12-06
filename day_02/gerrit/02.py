from data import read_lines


get_data = lambda: read_lines(2)


def map(items, fn):
    for item in items:
        yield fn(item)


def validate_count(policy, password):
    required_character, lower_bound, upper_bound = policy

    count = password.count(required_character)

    return lower_bound <= count and count <= upper_bound


def validate_position(policy, password):
    required_character, pos_1, pos_2 = policy

    character_at = lambda index: password[index-1]
    matching     = lambda char: 1 if char == required_character else 0

    occurences = matching(character_at(pos_1)) + matching(character_at(pos_2))

    return occurences == 1


def tokenize(line):
    policy_string, password           = line.split(": ")
    bounds       , required_character = policy_string.split(" ")
    first        , second             = bounds.split("-")

    return [[required_character, int(first), int(second)], password]


def valid_passwords(data, validator):
    return filter(map(data, tokenize), validator)


print(len([
    password
    for policy, password in map(get_data(), tokenize) if validate_count(policy, password)
]))

print(len([
    password
    for policy, password in map(get_data(), tokenize) if validate_position(policy, password)
]))
