
in_file = "input.txt"


def read_input_lines():
    with open(in_file, 'r') as fh:
        return [x.strip() for x in fh.readlines()]


def data_to_dict():
    data_dict={}
    for i,n in enumerate(read_input_lines()):
        data_dict[i]= [n[:3],int(n[3:]),0]
    return data_dict

def __parser(data,pos,accumulator):
    command = data[pos][0]
    value = data[pos][1]
    visits = data[pos][2]
    if visits == 1:
        return pos,accumulator,False

    data[pos][2] = 1

    if command == "acc":
        accumulator += value
        pos += 1
    elif command == "jmp":
        pos += value
    elif command == "nop":
        pos += 1
    return pos,accumulator,True

def puzzle1():
    data=data_to_dict()
    accumulator=0
    pos=0
    state=1
    while state:
        pos,accumulator,state=__parser(data,pos,accumulator)
    print(f"Accumulator value: {accumulator}")

def puzzle2():
    data = data_to_dict()
    prog_len = len(data.keys())

    for k,v in data.items():
        data_new=data_to_dict()
        accumulator = 0
        pos = 0

        if v[0] == "jmp":
            data_new[k][0] = "nop"
        if v[0] == "nop":
            data_new[k][0] = "jmp"
        if data_new[k][0] != v[0]:
            state = 1
            while state:
                pos, accumulator, state = __parser(data_new, pos, accumulator)
                if pos == prog_len:
                    print(f"Accumulator value: {accumulator}")
                    break


if __name__ == '__main__':
   puzzle1()
   puzzle2()
