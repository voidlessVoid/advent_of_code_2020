from functools import reduce

from data import read_lines

from util.matrix import (
    matrix_get,
    out_of_bounds,
    traverse_matrix
)

from util.iterators import (
    trajectory,
    trajectory_fixpoint,
    assert_trajectory_correctness,
)


real_data = list(read_lines(11))


test_data = [
    "L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",
    "L.LLLLL.LL",
]


# ------------------------------------
# Part 1


def adjacency_neighbourhood(matrix):
    def get_neighbourhood(x, y):
        deltas = [-1, 0, 1]

        return [
            [
                matrix_get(matrix, ".")(x + dx, y + dy)
                for dy in deltas
            ]
            for dx in deltas
        ]

    return get_neighbourhood


def count_seats(matrix, char):
    return sum(row.count(char) for row in matrix)


def seating_rule(neighbourhood, threshold):
    seating_rules = {
        ".": lambda: ".",
        "L": lambda: (
            "#" if count_seats(neighbourhood, "#") == 0
            else "L"
        ),
        "#": lambda: (
            "L" if count_seats(neighbourhood, "#") > threshold
            else "#"
        ),
    }

    return seating_rules[neighbourhood[1][1]]()


def apply_seating_rule(
    neighbourhood,
    threshold
):
    def rule(matrix):
        return [
            [
                seating_rule(neighbourhood(matrix)(x, y), threshold)
                for y in range(len(matrix[x]))
            ]
            for x in range(len(matrix))
        ]

    return rule


seating_rule_1 = apply_seating_rule(
    adjacency_neighbourhood,
    threshold=4
)


def part_1(matrix):
    return count_seats(trajectory_fixpoint(seating_rule_1)(matrix), "#")


# Unit tests part 1


def assert_state_equality(processed, string_notated):
    converted = ["".join(x) for x in processed]

    if not converted == string_notated:
        print("assertion failed: states not equal")

        for l, r in zip(converted, string_notated):
            print(*["\t", l, "\t", r], *([] if l == r else "\t!"))

        raise AssertionError("assertion failed: states not equal")

    return


assert_trajectory_correctness(seating_rule_1, assert_state_equality)(test_data, [
    [
        "#.##.##.##",
        "#######.##",
        "#.#.#..#..",
        "####.##.##",
        "#.##.##.##",
        "#.#####.##",
        "..#.#.....",
        "##########",
        "#.######.#",
        "#.#####.##",
    ],
    [
        "#.LL.L#.##",
        "#LLLLLL.L#",
        "L.L.L..L..",
        "#LLL.LL.L#",
        "#.LL.LL.LL",
        "#.LLLL#.##",
        "..L.L.....",
        "#LLLLLLLL#",
        "#.LLLLLL.L",
        "#.#LLLL.##",
    ],
    [
        "#.##.L#.##",
        "#L###LL.L#",
        "L.#.#..#..",
        "#L##.##.L#",
        "#.##.LL.LL",
        "#.###L#.##",
        "..#.#.....",
        "#L######L#",
        "#.LL###L.L",
        "#.#L###.##",
    ],
    [
        "#.#L.L#.##",
        "#LLL#LL.L#",
        "L.L.L..#..",
        "#LLL.##.L#",
        "#.LL.LL.LL",
        "#.LL#L#.##",
        "..L.L.....",
        "#L#LLLL#L#",
        "#.LLLLLL.L",
        "#.#L#L#.##",
    ],
    [
        "#.#L.L#.##",
        "#LLL#LL.L#",
        "L.#.L..#..",
        "#L##.##.L#",
        "#.#L.LL.LL",
        "#.#L#L#.##",
        "..L.L.....",
        "#L#L##L#L#",
        "#.LLLLLL.L",
        "#.#L#L#.##",
    ]
])


# Output part 1


assert part_1(test_data) == 37


print("Running part 1")
result_part_1 = part_1(real_data)
print("\t", result_part_1)


assert result_part_1 == 2338


# ------------------------------------
# Part 2


def los_neighbourhood(matrix):
    # print("LOS")
    def neighbourhood(x, y):
        def observe_seat(dx, dy):
            # print("calc", (dx, dy))
            if [dx, dy] == [0, 0]:
                # print("\tcenter", matrix[x][y])
                return matrix[x][y]

            for field in traverse_matrix(matrix)(x, y, dx, dy):
                # print("\tlooking", field)
                if field == None:
                    return "."

                if field in ["L", "#"]:
                    return field

        deltas = [-1, 0, 1]

        return [
            [
                observe_seat(dx, dy)
                for dy in deltas
            ]
            for dx in deltas
        ]

    return neighbourhood


seating_rule_2 = apply_seating_rule(
    los_neighbourhood,
    threshold=5,
)


def part_2(matrix):
    return count_seats(trajectory_fixpoint(seating_rule_2)(matrix), "#")


# Unit tests part 2


assert_trajectory_correctness(seating_rule_2, assert_state_equality)(test_data, [
    [
        "#.##.##.##",
        "#######.##",
        "#.#.#..#..",
        "####.##.##",
        "#.##.##.##",
        "#.#####.##",
        "..#.#.....",
        "##########",
        "#.######.#",
        "#.#####.##",
    ],
    [
        "#.LL.LL.L#",
        "#LLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLL#",
        "#.LLLLLL.L",
        "#.LLLLL.L#",
    ],
    [
        "#.L#.##.L#",
        "#L#####.LL",
        "L.#.#..#..",
        "##L#.##.##",
        "#.##.#L.##",
        "#.#####.#L",
        "..#.#.....",
        "LLL####LL#",
        "#.L#####.L",
        "#.L####.L#",
    ],
    [
        "#.L#.L#.L#",
        "#LLLLLL.LL",
        "L.L.L..#..",
        "##LL.LL.L#",
        "L.LL.LL.L#",
        "#.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLL#",
        "#.LLLLL#.L",
        "#.L#LL#.L#",
    ],
    [
        "#.L#.L#.L#",
        "#LLLLLL.LL",
        "L.L.L..#..",
        "##L#.#L.L#",
        "L.L#.#L.L#",
        "#.L####.LL",
        "..#.#.....",
        "LLL###LLL#",
        "#.LLLLL#.L",
        "#.L#LL#.L#",
    ],
    [
        "#.L#.L#.L#",
        "#LLLLLL.LL",
        "L.L.L..#..",
        "##L#.#L.L#",
        "L.L#.LL.L#",
        "#.LLLL#.LL",
        "..#.L.....",
        "LLL###LLL#",
        "#.LLLLL#.L",
        "#.L#LL#.L#",
    ],
])


# Output part 2


assert part_2(test_data) == 26


print("Running part 2")
result_part_2 = part_2(real_data)
print("\t", result_part_2)


# assert result_part_1 == 2338
