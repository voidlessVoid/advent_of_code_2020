data = [2, 0, 6, 12, 1, 3]


def puzzle1(data, value=2020):
    turn_dict = {}
    for i, x in enumerate(data):
        turn_dict[x] = (i + 1, i + 1)
    last_turn_nr = data[-1]
    turn = len(data) + 1
    while not turn > value:
        p, l = turn_dict[last_turn_nr]
        if p - l == 0:
            turn_nr = 0
        else:
            turn_nr = l - p
        if turn_nr in turn_dict.keys():
            turn_dict[turn_nr] = (turn_dict[turn_nr][1], turn)
        else:
            turn_dict[turn_nr] = (turn, turn)
        last_turn_nr = turn_nr
        print(f"Turn {turn}", end="\r")
        turn += 1

    print(f"Turn {turn}: Number= {last_turn_nr}")


def puzzle2(data, value):
    puzzle1(data, value)


if __name__ == '__main__':
    puzzle1(data)
    puzzle2(data, value=30000000)
