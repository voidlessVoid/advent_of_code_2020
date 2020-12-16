from data import read_lines

from util import split_by, prod


real_data = list(read_lines(16))


test_data = [
    "class: 1-3 or 5-7",
    "row: 6-11 or 33-44",
    "seat: 13-40 or 45-50",
    "",
    "your ticket:",
    "7,1,14",
    "",
    "nearby tickets:",
    "7,3,47",
    "40,4,50",
    "55,2,20",
    "38,6,12",
]


# Parsing


def parse_range(r):
    lb, ub = r.split("-")

    return [int(lb), int(ub)]


def parse_header_line(line):
    field, rest = line.split(": ")
    lower, upper = rest.split(" or ")

    return [field, [parse_range(lower), parse_range(upper)]]


def parse_header(raw):
    items = [
        parse_header_line(line)
        for line in raw
    ]

    return { field: ranges for field, ranges in items }


def parse_ticket_line(line):
    return [int(i) for i in line.split(",")]


def parse_ticket(raw):
    assert raw[0] == "your ticket:"

    return parse_ticket_line(raw[1])


def parse_context(raw):
    assert raw[0] == "nearby tickets:"

    return [
        parse_ticket_line(line)
        for line in raw[1:]
    ]


def parse(data):
    raw_header, raw_ticket, raw_context = split_by(lambda l: l == "")(data)

    return [
        parse_header(raw_header),
        parse_ticket(raw_ticket),
        parse_context(raw_context),
    ]


# Validation


def validate_ranges(ranges, value):
    return any(
        lb <= value <=ub
        for lb, ub in ranges
    )


def is_valid_value(header, value):
    return any(
        validate_ranges(ranges, value)
        for field, ranges in header.items()
    )


def is_valid_ticket(header, ticket):
    return all(
        is_valid_value(header, value)
        for value in ticket
    )


# Transformations


def values_by_field(tickets):
    assert len(tickets) >= 1

    return [
        [ticket[index] for ticket in tickets]
        for index in range(len(tickets[0]))
    ]


def possible_fields(header, values):
    return [
        field
        for field, ranges in header.items()
        if all(
            validate_ranges(ranges, value)
            for value in values
        )
    ]


def locate_fields(remaining_candidates, accumulator={}):
    located = {
        index: candidates[0]
        for index, candidates in enumerate(remaining_candidates)
        if len(candidates) == 1
    }

    if len(located) == 0:
        assert all(len(candidates) == 0 for candidates in remaining_candidates)
        return accumulator

    return locate_fields(
        remaining_candidates=[
            [field for field in candidates if field not in located.values()]
            for candidates in remaining_candidates
        ],
        accumulator={**accumulator, **located}
    )


def field_order(header, valid_tickets):
    candidates_by_index = [
        possible_fields(header, values)
        for values in values_by_field(valid_tickets)
    ]

    field_by_index = locate_fields(candidates_by_index)

    return [
        field_by_index[index]
        for index in range(len(field_by_index))
    ]


# Part 1


def part_1(data):
    header, ticket, context = parse(data)

    invalid_values = [
        value
        for ticket in context
        for value in ticket
        if not is_valid_value(header, value)
    ]

    return sum(invalid_values)


assert part_1(test_data) == 71


print("Part 1:", part_1(real_data))


# Part 2


test_data_2 = [
    "class: 0-1 or 4-19",
    "row: 0-5 or 8-19",
    "departure seat: 0-13 or 16-19",
    "",
    "your ticket:",
    "11,12,13",
    "",
    "nearby tickets:",
    "3,9,18",
    "15,1,5",
    "5,14,9",
]


def part_2(data):
    header, owned_ticket, context = parse(data)

    valid_tickets = [
        ticket
        for ticket in [owned_ticket, *context]
        if is_valid_ticket(header, ticket)
    ]

    ticket_data = dict(zip(
        field_order(header, valid_tickets),
        owned_ticket
    ))

    return prod([
        value
        for field, value in ticket_data.items()
        if field.startswith("departure")
    ])


assert part_2(test_data_2) == 13


print("Part 2:", part_2(real_data))
