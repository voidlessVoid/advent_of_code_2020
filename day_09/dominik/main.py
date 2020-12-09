from itertools import combinations
in_file = "input.txt"


def read_input_lines():
    with open(in_file, 'r') as fh:
        return [int(x.strip()) for x in fh.readlines()]

def _datacycle(data,data_range):
    data_cycle= data[data_range[0]:data_range[1]]
    valid=[]
    for pair in combinations(data_cycle,2):
        valid.append(sum(pair))
    return set(valid)

def puzzle1(preamble=25):
    data= read_input_lines()
    preamble_pos=[0,preamble]
    while True:
        if data[preamble_pos[1]] in _datacycle(data,preamble_pos):
            preamble_pos=[x+1 for x in preamble_pos]
        else:
            break
    print(f"First number out of the row: index: {preamble_pos[1]}, value: {data[preamble_pos[1]]}")



def puzzle2(breakvalue=85848519):
    data = read_input_lines()
    i=0 # avoiding the local variable might be referenced before assignment message
    span = 2
    while span < len(data)+1:
        for i,n in enumerate(data):
            SUM=sum(data[i:i+span])
            if SUM==breakvalue:
                break
        else:
            span += 1
            continue
        break
    match=data[i:i+span]
    print(f"Encryption weakness is: {min(match)+max(match)}")

if __name__ == '__main__':
   puzzle1()
   puzzle2()
