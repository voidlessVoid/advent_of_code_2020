from data import read_lines

from util import split_by, pipe, filter


real_data = list(read_lines(4))


test_data = [
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
    "byr:1937 iyr:2017 cid:147 hgt:183cm",
    "",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
    "hcl:#cfa07d byr:1929",
    "",
    "hcl:#ae17e1 iyr:2013",
    "eyr:2024",
    "ecl:brn pid:760753108 byr:1931",
    "hgt:179cm",
    "",
    "hcl:#cfa07d eyr:2025 pid:166559648",
    "iyr:2011 ecl:brn hgt:59in",
]

test_invalids = [
    "eyr:1972 cid:100",
    "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
    "",
    "iyr:2019",
    "hcl:#602927 eyr:1967 hgt:170cm",
    "ecl:grn pid:012533040 byr:1946",
    "",
    "hcl:dab227 iyr:2012",
    "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
    "",
    "hgt:59cm ecl:zzz",
    "eyr:2038 hcl:74454a iyr:2023",
    "pid:3556412378 byr:2007",
]

test_valids = [
    "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
    "hcl:#623a2f",
    "",
    "eyr:2029 ecl:blu cid:129 byr:1989",
    "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
    "",
    "hcl:#888785",
    "hgt:164cm byr:2001 iyr:2015 cid:88",
    "pid:545766238 ecl:hzl",
    "eyr:2022",
    "",
    "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
]


numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
hex_digits = [
    *numbers,
    *["a", "b", "c", "d", "e", "f"]
]


def is_between(a, b):
    return lambda x: a <= int(x) and int(x) <= b


def validate_height(h):
    num = h[:-2]
    suffix = h[-2:]

    return (
        suffix in ["cm", "in"] and num.isnumeric()
        and (
            is_between(150, 193)(num) if suffix == "cm"
            else is_between(59, 76)(num)
        )
    )


validators = {
    "byr": lambda x: (
        len(x) is 4 and is_between(1920, 2002)(x)
    ),
    "iyr": lambda x: (
        len(x) is 4 and is_between(2010, 2020)(x)
    ),
    "eyr": lambda x: (
        len(x) is 4 and is_between(2020, 2030)(x)
    ),
    "hgt": validate_height,
    "hcl": lambda x: (
        x[:1] is "#"
        and all(c in hex_digits for c in x[1:])
    ),
    "ecl": lambda x: (
        x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    ),
    "pid": lambda x: (
        len(x) is 9
        and all(c in numbers for c in x)
    )
}

required_fields = list(validators.keys())


def contained_in(small, big):
    contained = [x for x in small if x in big]
    return small == contained


def build_passport(raw_passport):
    return {
        k: v
        for k, v in [x.split(":") for x in raw_passport]
    }

def passports(data):
    return [
        build_passport(" ".join(block).split(" "))
        for block in split_by(lambda x: x is "")(data)
    ]


def validate_with(validators):
    def validator(entry):
        key, value = entry
        return validators.get(key, lambda x: True)(value)
    return validator


def is_valid(passport):
    return (
        contained_in(required_fields, passport.keys())
        and all(
            validate_with(validators)(entry)
            for entry in passport.items()
        )
    )



result = [
    [is_valid(passport), passport]
    for passport in passports(real_data)
]


assert not any (
    is_valid(passport)
    for passport in passports(test_invalids)
)

assert all(
    is_valid(passport)
    for passport in passports(test_valids)
)

print(len(list(
    filter(passports(real_data), is_valid)
)))
