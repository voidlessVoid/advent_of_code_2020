from itertools import product

in_file = "input.txt"


def read_input_lines():
    with open(in_file, 'r') as fh:
        return [x.strip() for x in fh.readlines()]


def seat_bubble():
    bubble = [x for x in product([-1, 0, 1], repeat=2)]
    bubble.pop(4)  # removing (0,0)
    return bubble


def adjacent_occupied(ri, si, layout):
    neighbours = seat_bubble()
    counter = 0
    # test for neighbours and cutting of the edge cases of the bubble
    for n in neighbours:
        r = ri + n[0]
        s = si + n[1]
        if r >= 0 and r < len(layout) and s >= 0 and s < len(layout[r]):
            counter += (layout[r][s] == "#")  # returns True and is interpreted as bool
    return counter


def adjacent_occupied_line_of_sight(ri, si, layout):
    neighbours = seat_bubble()
    counter = 0
    # test for neighbours and cutting of the edge cases of the bubble
    for n in neighbours:
        r = ri + n[0]
        s = si + n[1]
        while r >= 0 and r < len(layout) and s >= 0 and s < len(layout[r]) and layout[r][s] == '.':
            r += n[0]
            s += n[1]
        if r >= 0 and r < len(layout) and s >= 0 and s < len(layout[r]):
            counter += (layout[r][s] == "#")
    return counter


def seating_procedure(layout: list, func, occ_limits: tuple):
    temp = []
    counter = 0
    for ri in range(len(layout)):
        row = ''
        for si in range(len(layout[ri])):
            seat_state = layout[ri][si]
            if seat_state != '.':
                occupants = func(ri, si, layout)
                if seat_state == 'L' and occupants == occ_limits[0]:
                    seat_state = '#'
                if seat_state == '#' and occupants >= occ_limits[1]:
                    seat_state = 'L'
            row += seat_state
        temp.append(row)

    for l in temp:
        counter += l.count("#")
    return temp, counter


def puzzle1():
    layout = read_input_lines()

    counter = 0
    counter_old = 1
    while not counter == counter_old:
        counter_old = counter
        layout, counter = seating_procedure(layout=layout, func=adjacent_occupied, occ_limits=(0, 4))
        print(f"Occupied seats: {counter}", end="\r")
    print(f"Final number of occupied seats: {counter}")


def puzzle2():
    layout = read_input_lines()

    counter = 0
    counter_old = 1
    while not counter == counter_old:
        counter_old = counter
        layout, counter = seating_procedure(layout=layout, func=adjacent_occupied_line_of_sight, occ_limits=(0, 5))
        print(f"Occupied seats: {counter}", end="\r")
    print(f"Final number of occupied seats: {counter}")


if __name__ == '__main__':
    puzzle1()
    puzzle2()
    pass