from data import read_lines

from util import pipe
from util.matrix import array_get, plus, fill
from util.iterators import trajectory, take, get_nth


real_data = list(read_lines(17))


test_data = [
    ".#.",
    "..#",
    "###",
]


def init_state(base, dimensions):
    size = [
        len(base[0]),
        len(base),
        *[1 for d in range(2, dimensions)]
    ]

    def nest(n, x):
        return (
            x if n <= 0
            else [nest(n - 1, x)]
        )

    space = nest(dimensions - 2, base)

    return [dimensions, size, space]


def get(space, pos):
    return pipe(space)(*[
        array_get(p, [] if (i < len(pos) - 1) else ".")
        for i, p in enumerate(reversed(pos))
    ])


def adjacency_neighbourhood(space, pos):
    deltas = [-1, 0, 1]

    def recur(nb_pos=[], remaining_pos=pos):
        if len(remaining_pos) == 0:
            return get(space, nb_pos)
        else:
            return [
                recur(
                    [*nb_pos, remaining_pos[0] + d],
                    remaining_pos[1:]
                )
                for d in deltas
            ]

    return recur()


def count_blocks(space):
    if type(space) == str:
        return 1 if space == "#" else 0

    return sum(count_blocks(layer) for layer in space)


def progression_rule(neighbourhood):
    rules = {
        ".": lambda: (
            "#" if count_blocks(neighbourhood) == 3
            else "."
        ),
        "#": lambda: (
            "#" if count_blocks(neighbourhood) - 1 in [2, 3]
            else "."
        ),
    }

    def get_center(nb):
        return (
            nb if type(nb) == str
            else get_center(nb[1])
        )

    return rules[get_center(neighbourhood)]()


def progress(state):
    dimensions, size, space = state

    new_size = plus(size, fill(dimensions, 2))

    def recur_space(pos=[], layer=space, dim=dimensions - 1):
        if dim < 0:
            return progression_rule(
                adjacency_neighbourhood(space, pos)
            )
        else:
            return [
                recur_space(
                    [p, *pos],
                    array_get(p, [])(layer),
                    dim-1
                )
                for p in range(-1, size[dim] + 1)
            ]

    new_space = recur_space()

    return [dimensions, new_size, new_space]


def grow(base, dimensions, steps):
    state = init_state(base, dimensions)

    return get_nth(steps)(trajectory(progress)(state))


# Part 1


def part_1(data):
    dim, size, space = grow(data, 3, 6)

    return count_blocks(space)


assert part_1(test_data) == 112


result_1 = part_1(real_data)


print(result_1)


assert result_1 == 384


# Part 2


def part_2(data):
    dim, size, space = grow(data, 4, 6)

    return count_blocks(space)


assert part_2(test_data) == 848


print(part_2(real_data))
