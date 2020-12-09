def read_lines(number_of_day):
    with open(f"data/{number_of_day}.txt") as file:
        for line in file.readlines():
            yield line.rstrip()
