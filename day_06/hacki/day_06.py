

f_name = 'test_puzzle'
#f_name = 'puzzle_input'


def load_input_paragraphs(path):
    with open(path) as file:
        lines = file.read()
        paragraphs = [paragraph.split() for paragraph in lines.split("\n\n")]
        return paragraphs

in_ls = load_input_paragraphs(f_name)

def unionize(ls):
    return set().union(*ls)

def intersect(ls):
    return set().intersection(*ls)

part_a = 0
part_b = 0
for i in in_ls:
    part_a += len(unionize(i))
    print(part_a)
    print(unionize(i))
    i = [set(list(j)) for j in i]
    print(i)
    x = set().intersection(*i)

print(part_a)
