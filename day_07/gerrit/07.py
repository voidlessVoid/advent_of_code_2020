from util import compose, apply_to, flip

from data import read_lines


OWN_BAG_COLOR = "shiny gold"


real_data = list(read_lines(7))


test_data = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags.",
]

test_data_2 = [
    "shiny gold bags contain 2 dark red bags.",
    "dark red bags contain 2 dark orange bags.",
    "dark orange bags contain 2 dark yellow bags.",
    "dark yellow bags contain 2 dark green bags.",
    "dark green bags contain 2 dark blue bags.",
    "dark blue bags contain 2 dark violet bags.",
    "dark violet bags contain no other bags.",
]

def drop_last(*to_drop):
    def dropper(s):
        for td in to_drop:
            if s[-len(td):] == td:
                return s[:-len(td)]
        return s
    return dropper


def parse_rule(raw_rule):
    return dict(
        apply_to(item, compose(
            drop_last(" bag", " bags"),
            lambda i: i.split(" ", 1),
            flip
        ))
        for item in raw_rule.split(", ")
        if not item.startswith("no other")
    )


def parse_rules(data):
    return dict(
        apply_to(line, compose(
            drop_last("."),
            lambda s: s.split(" contain "),
            lambda i: [drop_last(" bags")(i[0]), parse_rule(i[1])],
        ))
        for line in data
    )


def can_contain(rules, rule, color):
    return (
        color in rule.keys()
        or any(
            can_contain(rules, rules[nested_color], color)
            for nested_color in rule.keys()
        )
    )


def count_contained(rules, color):
    return sum(
        int(count) + (int(count) * count_contained(rules, nested))
        for nested, count in rules[color].items()
    )


def part_1(data):
    rules = parse_rules(data)

    return len([
        color
        for color, rule in rules.items()
        if can_contain(rules, rule, OWN_BAG_COLOR)
    ])


def part_2(data):
    return count_contained(parse_rules(data), OWN_BAG_COLOR)


assert part_1(test_data) == 4


print(part_1(real_data))

assert part_2(test_data) == 32, f"td: {part_2(test_data)}"
assert part_2(test_data_2) == 126, f"td2: {part_2(test_data_2)}"

print(part_2(real_data))
