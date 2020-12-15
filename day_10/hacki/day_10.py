from misc_hacki import misc
import numpy as np
import itertools as it


def part_a(
        jolt_ls,
        lower_local_limit,
        upper_limit
):
    from collections import Counter

    lower_local_limit_ls = np.linspace(
        start = 1,
        stop = lower_local_limit,
        num = lower_local_limit
    ).astype(int)
    jolt_rating = 0
    difference = []
    while True:
        jolt_union = list(
            set(in_ls) & set(jolt_rating+lower_local_limit_ls)
        )
        temp_difference = [
            jolt - jolt_rating for jolt in jolt_union
        ]
        #print(temp_difference)
        if jolt_rating == max(in_ls):
            temp_difference = upper_limit
            difference.append(temp_difference)
            break
        else:
            difference.append(
                min(temp_difference)
            )
            jolt_rating += min(temp_difference)
            print(temp_difference, difference, jolt_rating)
    difference_dict = dict(
        zip(
            Counter(difference).keys(),
            Counter(difference).values()
        )
    )

    return difference, difference_dict, np.prod(
        [
            difference_dict[key] for key in difference_dict.keys()
        ]
    )


f_name = 'test_puzzle'
#f_name = 'puzzle_input'
in_ls = misc.load_input_to_list(f_name)

a = part_a(
    jolt_ls=in_ls,
    upper_limit=3,
    lower_local_limit = 3
)
print(a)

