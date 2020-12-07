from misc_hacki import misc

#f_name = 'test_puzzle'
f_name = 'puzzle_input'
util = misc.open_ngyu()
def load_input_paragraphs(path):
    with open(path) as file:
        lines = file.read()
        paragraphs = [
            paragraph.split() for paragraph in lines.split("\n\n")
        ]
        return paragraphs

def unionize(ls):
    return set().union(*ls)

def intersect(ls):
    return set(ls[0]).intersection(*ls)

if __name__ == '__main__':

    in_ls = load_input_paragraphs(f_name)
    part_a, part_b = 0, 0

    for i in in_ls:
        part_a += len(unionize(i))
        part_b += len(intersect(i))

    print(part_a, part_b)
