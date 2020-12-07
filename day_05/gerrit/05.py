from data import read_lines


data = list(read_lines(5))


def map_string(s, f):
    return "".join(f(c) for c in s)


def read_binary_string(characters):
    def reader(binary_string):
        return int(map_string(binary_string, remap(characters)), 2)

    return reader


def remap(characters):
    zero, one = characters

    def mapper(c):
        return "1" if c == one else "0"

    return mapper


def read_seat(seat_string):
    return [
        read_binary_string(["F", "B"])(seat_string[:-3]),
        read_binary_string(["L", "R"])(seat_string[-3:]),
    ]


def seat_id(seat_string):
    row, col = read_seat(seat_string)

    return row * 8 + col


def find_gaps(seat_ids):
    for x in range(min(seat_ids), max(seat_ids)):
        if x not in seat_ids:
            yield x


print(list(find_gaps([
    seat_id(line)
    for line in data
])))


