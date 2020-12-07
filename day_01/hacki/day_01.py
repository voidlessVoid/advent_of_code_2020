# great I should be more careful with my stars..
# two integers summed up should == 2020 and the multiplication is the answer of the first part.

# combinations
import itertools as it
import numpy as np
from misc_hacki import misc

in_ls = misc.load_input_to_list(misc.path_to_dir('puzzle_input'))
util = misc.open_nggyu()
# dummy input
sum_to_reach = 2020

# number of combinations
combinations = 3

# combination function
def comb(ls_input, comb_int):
    # return list comprehension with all combinations
    return [
        combination for combination in it.combinations(
            ls_input,
            comb_int
        )
    ]

# ls of tuples with all possible combinations
combination_ls = comb(
    ls_input=in_ls,
    comb_int=combinations
)

def generate_sum(ls_input, sum_to_reach):
    # returns the combination, sum of combination and multiplication
    # np.prod is the product of all elements in tuple
    global it_sum
    sum_list = [
        [
            i,
            sum(i),
            np.prod(i)
        ] for i in ls_input
    ]

    # checks for sum to reach and hands out ls, creates empty list

    check_sum_ls = []

    for it_sum in sum_list:
        if it_sum[1] == sum_to_reach:
            check_sum_ls.append(it_sum)

    return check_sum_ls

test = generate_sum(combination_ls, sum_to_reach)
print(test)