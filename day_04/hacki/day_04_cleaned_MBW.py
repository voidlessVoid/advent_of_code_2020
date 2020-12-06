import pandas as pd
import sqlite3 as sl3
import re



def create_passport_keys(ls_in):

    passports = [
        [
            (keys.split('\n')) for keys in passport
        ] for passport in ls_in
    ]

    passport_lists = []
    for passport in passports:
        key_list = []
        for key in passport:
            if len(key) >= 2:
                for k in key:
                    key_list.append([k])
            else:
                key_list.append(key)
        passport_lists.append(key_list)

    return passport_lists

def create_dict(p_ls_in):

    dict_ls = []

    for passport in p_ls_in:
        passport_keys = []
        for key in passport:
            for k in key:
                passport_keys.append(
                    tuple(k.split(':'))
                )
        dict_ls.append(
            dict(passport_keys)
        )

    return dict_ls

def check_passport(key_list, d_ls_in):

    first_order_valid_passports = []
    key_list.sort()
    for d in d_ls_in:
        d_set = list(key_list & d.keys())
        d_set.sort()
        if list(d_set) == key_list:
            first_order_valid_passports.append(d)

    return first_order_valid_passports

f_name = 'puzzle_input'

with open(f_name, 'r') as fh:
    passport_ls = [x.split() for x in fh.read().split("\n\n")]

passport_keys = create_passport_keys(
    ls_in=passport_ls
)

passport_dicts = create_dict(
    p_ls_in=passport_keys
)

valid_keys = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]

# noinspection PyTypeChecker
first_order_valid_passports = check_passport(
    key_list=valid_keys,
    d_ls_in=passport_dicts
)

conn = sl3.connect(":memory:")
conn.create_function('regexp', 2, lambda x, y: 1 if re.search(x, y) else 0)

def create_and_return_sql(dict, connect_name):

    print(pd.DataFrame(
            dict
        ))
    try:
        pd.DataFrame(
            dict
        ).to_sql(
            name = connect_name,
            con=conn
        )
    except:
        pass

    cur = conn.cursor()

    return cur

passport_db = create_and_return_sql(
    first_order_valid_passports,
    f_name
)

def count_valid(db_name):

    ecl_ls = (
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth',
    )

    query = f"""
        SELECT count(*) FROM 
        {db_name}
        WHERE
        cast(byr as int) BETWEEN 1920 AND 2002
        AND cast(iyr as int) BETWEEN 2010 AND 2020
        AND cast(eyr as int) BETWEEN 2020 AND 2030
        AND (
              ((hgt like '%cm' ) and (cast(substr(hgt,1,length(hgt) - 2) as int) BETWEEN 150 and 193)) 
              or
              ((hgt like '%in') and (cast(substr(hgt,1,length(hgt) - 2) as int) BETWEEN 59 and 76))
            )
        AND hcl regexp '(^#[a-f0-9]{{6}}$)'
        AND ecl in {str(ecl_ls)}
        AND pid regexp '^\d{{9}}$'
    """

    print(query)
    filtered_db = pd.read_sql_query(query, conn)

    return filtered_db


x = count_valid(db_name = f_name)
conn.close()
print(x)