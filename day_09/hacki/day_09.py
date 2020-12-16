from misc_hacki import misc
import itertools as it


#day_01.comb()


# combination function
def sum_comb(ls_input, comb_int):
    # return list comprehension with all combinations
    return [
            sum(combination) for combination in it.combinations(
            ls_input,
            comb_int
        )
    ]


def part_a(
        in_ls,
        preamble,
        combinations
):

    global break_number
    index = 0

    while index+preamble <= len(in_ls)-1:
        ls = in_ls[
             index:(index+preamble)
             ]

        comb_ls = sum_comb(
            ls_input=ls,
            comb_int=combinations,
        )

        if in_ls[index+preamble] not in comb_ls:
            break_number = in_ls[index+preamble]
            break
        if in_ls[index+preamble] in comb_ls:
            index += 1

    return break_number


def part_b(
        in_ls,
        invalid_n,
        combinations
):
    global encryption_weakness_sum
    range_n = 2
    index = 0

    while index+range_n <= len(in_ls)-1:

        if index + range_n == len(in_ls) - 1:
            index = 0
            range_n += 1
        ls = in_ls[
             index:(index + range_n)
             ]
        if sum(ls) == invalid_n:
            encryption_weakness_sum = min(ls)+max(ls)
        index +=1

    return encryption_weakness_sum


#f_name = 'test_puzzle'
f_name = 'puzzle_input'
in_ls = misc.load_input_to_list(f_name)
preamble = 25
combinations = 2

invalid_number = part_a(
    in_ls=in_ls,
    preamble = preamble,
    combinations = combinations
)

print(invalid_number)

encryption_weakness = part_b(
    in_ls=in_ls,
    invalid_n = invalid_number,
    combinations = combinations
)

print(encryption_weakness)

