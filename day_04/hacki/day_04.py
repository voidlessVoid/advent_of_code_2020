from misc_hacki import misc
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

f_name = 'test_puzzle'

passport_ls = misc.load_input_paragraphs(f_name)

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

    try:
        passport_df = pd.DataFrame(
            first_order_valid_passports
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

def filter_db(db_name):

    select_Statement = """
        SELECT * FROM 
        """ + db_name + """
            WHERE
        """
    byr_filter = """
        byr BETWEEN '1920' AND '2002' 
        """
    iyr_filter = """
        AND iyr BETWEEN '2010' AND '2020'
        """
    eyr_filter = """
        AND eyr BETWEEN '2020' AND '2030'
    """
    hgt_filter = """
        AND hgt BETWEEN '150cm' AND '193cm' or hgt BETWEEN '59in' AND '76in'
    """
    hcl_filter = """
        AND hcl regexp '(#[a-z0-9]{6}$)'
    """
    ecl_ls = (
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth',
    )
    ecl_filter = """
        AND ecl in 
    """ + str(ecl_ls)
    pid_filter = """
        AND pid regexp '(\d{9})'
    """

    # and hcl regexp '[a-z0-9]{6}$'

    query = select_Statement+byr_filter+iyr_filter+eyr_filter+hgt_filter+ecl_filter+hcl_filter+pid_filter

    filtered_db = pd.read_sql_query(query, conn)

    return filtered_db

pd.set_option('display.max_rows', None)

x = filter_db(db_name = f_name)
print(x)