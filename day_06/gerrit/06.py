from functools import reduce

from data import read_lines

from util import split_by


real_data = list(read_lines(6))


test_data = [
    "abc",
    "",
    "a",
    "b",
    "c",
    "",
    "ab",
    "ac",
    "",
    "a",
    "a",
    "a",
    "a",
    "",
    "b",
]


def sum(items):
    return reduce(
        lambda x, y: x + y,
        items,
        0
    )


def part_1(data):
    question_counts = [
        len(set(c for c in "".join(group)))
        for group in split_by(lambda x: x == "")(data)
    ]

    print("part 1", sum(question_counts))


def part_2(data):
    def shared_anwsers(group):
        all_answers = set(c for c in "".join(group))

        return [
            a
            for a in all_answers
            if all(a in form for form in group)
        ]

    shared = [
        len(shared_anwsers(group))
        for group in split_by(lambda x: x == "")(data)
    ]

    print("part 2", sum(shared))



part_1(real_data)
part_2(real_data)
