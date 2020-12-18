from .iterators import nats


def out_of_bounds(matrix):
    def oob(x, y):
        return (
            x < 0 or y < 0
            or x >= len(matrix) or y >= len(matrix[x])
        )

    return oob


def matrix_get(matrix, fallback=None):
    def getter(x, y):
        return (
            fallback if out_of_bounds(matrix)(x, y)
            else matrix[x][y]
        )

    return getter


def traverse_matrix(matrix):
    def traverse(x, y, dx, dy):
        if [dx, dy] == [0, 0]:
            yield matrix_get(matrix)(x, y)
            return

        for n in nats(1):
            xpos = x + n * dx
            ypos = y + n * dy

            value = matrix_get(matrix)(xpos, ypos)
            yield value

            if value == None:
                return

    return traverse


def array_get(index, fallback=None):
    def getter(array):
        if 0 <= index < len(array):
            return array[index]
        return fallback
    return getter


def plus(v1, v2):
    return [
        v1[dim] + v2[dim]
        for dim in range(len(v1))
    ]


def fill(len, x):
    return [x for _ in range(len)]
