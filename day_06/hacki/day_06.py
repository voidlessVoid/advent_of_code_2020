

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
    return set(ls[0]).intersection(*ls)

part_a = 0
part_b = 0
for i in in_ls:
    part_a += len(unionize(i))
    i = [list(j) for j in i]
    part_b += len(intersect(i))

print(part_a, part_b)
