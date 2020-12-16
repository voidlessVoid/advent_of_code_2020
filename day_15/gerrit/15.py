from util.iterators import take


test_data = [0, 3, 6]


real_data = [0, 3, 1, 6, 7, 5]


# Part 2


def part_1_generator(data):
    turns_spoken = {}
    last_number = None
    turn = 0

    def say_number(n):
        nonlocal last_number
        last_number = n
        turns_spoken[n] = (
            [turn] if n not in turns_spoken
            else [turns_spoken[n][-1], turn]
        )

        return n

    def spoken_once(n):
        return len(turns_spoken.get(n, [])) == 1

    for s in data:
        turn = turn + 1

        yield say_number(s)

    while True:
        turn = turn + 1

        yield say_number(
            0 if spoken_once(last_number)
            else turns_spoken[last_number][-1] - turns_spoken[last_number][-2]
        )


def part_1(data):
    for index, value in enumerate(part_1_generator(data)):
        if index + 1 == 2020:
            return value


expected_test_output = [0, 3, 6, 0, 3, 3, 1, 0, 4, 0]
actual_test_output = list(take(len(expected_test_output))(part_1_generator(test_data)))


for x in zip(expected_test_output, actual_test_output):
    print(x)


assert actual_test_output == expected_test_output


assert part_1(test_data) == 436


print(part_1(real_data))


# Part 2

def part_2(data):
    print("part 2", data)
    for index, value in enumerate(part_1_generator(data)):
        if index % 1000000 == 0:
            print("\t", index / 30000000)
        if index + 1 == 30000000:
            return value


# assert part_2([0, 3, 6]) == 175594
# assert part_2([1, 3, 2]) == 2578
# assert part_2([2, 1, 3]) == 3544142
# assert part_2([1, 2, 3]) == 261214
# assert part_2([2, 3, 1]) == 6895259
# assert part_2([3, 2, 1]) == 18
# assert part_2([3, 1, 2]) == 362


print(part_2(real_data))
