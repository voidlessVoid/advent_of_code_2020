# check password policy

from misc_hacki import misc
from string import punctuation  # returns special characters
import pandas as pd


# allows for having a list of split separators rather then one
def split_ls(txt, seps):
    default_sep = seps[0]

    # we skip seps[0] because that's the default separator
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    return [
        i.strip() for i in txt.split(default_sep)
    ]


def split_and_define(input, first_level, second_level):
    policy_pw_ls = [split_ls(i, seps=first_level) for i in input]
    policy_pw_df = pd.DataFrame(policy_pw_ls, columns=['req', 'character', 'pw'])
    policy_pw_df['req'] = policy_pw_df['req'].apply(split_ls, seps=second_level)

    policy_pw_df['character'] = policy_pw_df['character'].str.split(':', expand=True)

    req_df = policy_pw_df['req'].apply(pd.Series).astype(int)
    req_df.columns = ['min', 'max']

    pw_ls = list(policy_pw_df['pw'].str.split(''))
    pw_ls = [list(filter(None, i)) for i in pw_ls]
    policy_pw_df['pw'] = pw_ls

    return policy_pw_df.join(req_df).drop(columns=['req'])


def check_validity(df):
    ind_ls = []

    for char, pw in zip(df['character'], df['pw']):
        try:
            ind_ls.append([i + 1 for i, x in enumerate(pw) if x == char])
        except:
            pass

    df['indices'] = ind_ls

    valid_ls_c = []
    valid_ls_p = []

    for c_min, c_max, indices in zip(df['min'], df['max'], df['indices']):
        if len(indices) >= c_min:
            if len(indices) <= c_max:
                valid_ls_c.append(True)
            else:
                valid_ls_c.append(False)
        else:
            valid_ls_c.append(False)

    for pos_1, pos_2, indices in zip(df['min'], df['max'], df['indices']):
        set_list_1 = [{pos_1, pos_2}, set(indices)]
        set_list_2 = set_list_1[0] & set_list_1[1]
        if len(set_list_2) == 1:
            valid_ls_p.append(True)
        else:
            valid_ls_p.append(False)

    df['valid_c'], df['valid_p'] = valid_ls_c, valid_ls_p
    df['pw'] = df['pw'].str.join('')
    return df


in_ls = misc.load_input_to_list(
    misc.path_to_dir('puzzle_input')
)

special_characters = list(punctuation)  # list of special characters

first_level_sep = [' ']  # separator of puzzle input ls
second_level_sep = special_characters  # special characters second level split

pw_df = split_and_define(
    input=in_ls,
    first_level=first_level_sep,
    second_level=second_level_sep
)

valid_df = check_validity(pw_df)

part_1 = valid_df.loc[valid_df['valid_c'] == True]
part_2 = valid_df.loc[valid_df['valid_p'] == True]

print(part_1, part_2)
