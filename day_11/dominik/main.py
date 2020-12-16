in_file="input.txt"

def read_input_lines():
    with open(in_file, 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def puzzle1():
    layout=read_input_lines()

    def _bubble(seat_index, row_index, row, layout):
        seat_range = [seat_index + x for x in [-1, 0, 1] if seat_index + x >= 0 and seat_index + x < len(row)]
        row_range = [row_index + x for x in [-1, 0, 1] if row_index + x >= 0 and row_index + x < len(layout)]
        bubble= {}
        for r in row_range:
            bubble[r]=seat_range
        return bubble

    def move(layout):
        temp = [[0] * len(layout[0]) for _ in range(len(layout))]
        for ri,row in enumerate(layout):
            for si, seat in enumerate(row):
                char_count = 0
                seat_bubble=_bubble(si,ri,row,layout)
                for key, item in seat_bubble.items():
                    char_count+=layout[key][min(item):max(item) + 1].count("#")
                if layout[ri][si] == ".":
                    temp[ri][si] = '.'
                if layout[ri][si] == "#":
                    for key, item in seat_bubble.items():
                        for value in item:
                            if not key == ri and not value == si:
                                if char_count >4 :
                                    temp[ri][si] = "L"
                                else: temp[ri][si] = "#"
                if layout[ri][si] == "L":
                    for key, item in seat_bubble.items():
                        for value in item:
                            if not key == ri and not value == si:
                                if char_count ==0 :
                                    temp[ri][si] = "#"
                                else: temp[ri][si] = "L"

        counter=0
        for l in temp:
            counter+=l.count("#")
        return temp, counter

    counter=0
    counter_old=1
    while not counter==counter_old:
        counter_old = counter
        layout,counter=move(layout)
        print(f"Occupied seats: {counter}",end="\r")

def puzzle2():
    pass

if __name__ == '__main__':
    result=puzzle1()