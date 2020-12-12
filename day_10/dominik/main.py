from copy import deepcopy
from multiprocessing.dummy import Pool as ThreadPool
in_file = "input.txt"


def read_input_lines():
    with open(in_file, 'r') as fh:
        return [int(x.strip()) for x in fh.readlines()]

def chain(data):
    diffs = []
    for i, n in zip(data[:-1], data[1:]):
        diffs.append(n - i)
    return data, diffs

def extend_chain():
    data = read_input_lines()
    data.append(0)
    data.append(max(data) + 3)
    data.sort()
    return data

def puzzle1():
    in_data= extend_chain()
    _,diff_list=chain(in_data)

    print(f"Number of 1jolt diff: {diff_list.count(1)}, Number of 3jolt diff: {diff_list.count(3)}, Result: {diff_list.count(1) * diff_list.count(3)}")

def puzzle2():
    in_data = extend_chain()
    print(in_data)
    # get longest solution, or solution of puzzle a
    solutions=[[*chain(data=in_data)]]

    def __validate(in_data):
        data, diff_list = chain(in_data)
        if all(n == 1 or n == 2 or n == 3 for n in diff_list):
            return [data,diff_list]

    for line in solutions:
        for i,n in enumerate(line[1]):
            if n == 1:
                line_temp = deepcopy(line)
                line_temp[0].pop(i+1)
                validate= __validate(line_temp[0])
                if not validate == None and validate not in solutions:
                    solutions.append(validate)
                    print(f"Found valid solution: {len(solutions)}",end="\r")
                else: continue
    print(f"Total number of possible solutions: {len(solutions)}")

def puzzle21():
    in_data = extend_chain()
    _range=[1,2,3]
    #print(in_data[::-1])
    lvl_dict={}

    for n in range(len(in_data)):
        for i in [in_data[n]+x for x in _range]:
            if i in in_data:
                if n not in lvl_dict.keys():
                    lvl_dict[n]=[i]
                else:
                    lvl_dict[n].append(i)
    combinations=[]
    for i,pos in enumerate(in_data[:0:-1]):
        if len(lvl_dict[len(lvl_dict)-1-i])>1:
            for n in lvl_dict[len(lvl_dict)-1-i]:
                temp=deepcopy(in_data)[::-1]
                temp[i]= n
                combinations.append(temp)#list(set(temp)))
    print(*combinations,sep="\n")
    print(len(combinations)+1)
    return lvl_dict

def part_b():
        """ differences of 3 are like checkpoints where only one option is present
        here total permutations = permutations left * permutations right"""

        def calcPermute(numbers):
            return calcPermuteHelper(set(numbers), set(), numbers[0], numbers[-1])

        def calcPermuteHelper(numbers, visited, current, goal):
            if current == goal:
                return 1
            visited = deepcopy(visited)
            visited.add(current)
            next_options = ({current - x for x in [-2, -1, 1, 2, 3]} & numbers) - visited
            return sum(calcPermuteHelper(numbers, visited, x, goal) for x in next_options)

        def solve(numbers):
            try:
                nextdelta3ix = next((i for i in range(1, len(numbers)) if numbers[i] - numbers[i - 1] == 3))
                return calcPermute(numbers[:nextdelta3ix]) * solve(numbers[nextdelta3ix:])
            except StopIteration:
                return calcPermute(numbers)

        numbers = [0] + sorted([int(x) for x in read_input_lines()])

        print(solve(numbers))




if __name__ == '__main__':
    puzzle1()
    #part_b()