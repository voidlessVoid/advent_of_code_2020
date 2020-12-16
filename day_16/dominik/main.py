import re
from functools import reduce
from itertools import groupby

import numpy as np

in_file = "input.txt"


def read_input_lines():
    with open(in_file, 'r') as f:
        data = [x.strip() for x in f.readlines()]
    data.append("")
    return data


def format_input(in_list):
    ticketdata_list = (list(data_line) for _, data_line in groupby(in_list, key=''.__ne__))
    return [a + b for a, b in zip(ticketdata_list, ticketdata_list)]


def extract_rules(rules_raw):
    rule_pattern = re.compile("^(\w+|\w+ \w+): (\d+)-(\d+) or (\d+)-(\d+)$")
    rule_dict = {}
    for rule in rules_raw[:-1]:
        rule_data = re.match(rule_pattern, rule)
        rule_dict[rule_data.group(1)] = ((int(rule_data.group(2)), int(rule_data.group(3))), (int(rule_data.group(4)), int(rule_data.group(5))))
    return rule_dict


def validate_tickets(tickets_raw, comp_list):
    result = []
    filter_list = []
    ticket_list = tickets_raw[1:-1]
    for i, ticket in enumerate(ticket_list):
        ticket = [int(d) for d in ticket.split(',')]
        for value in ticket:
            if value not in comp_list:
                result.append(value)
                filter_list.append(i)

    filter_list = sorted(list(set(filter_list)))
    for i in filter_list[::-1]:
        ticket_list.pop(i)

    return sum(result), ticket_list


def puzzle1():
    in_list = read_input_lines()
    rules_raw, own_ticket, tickets_raw = format_input(in_list)
    own_ticket = own_ticket[1:-1]

    rule_dict = extract_rules(rules_raw=rules_raw)

    comp_list = []
    for rule in rule_dict.values():
        for rule_set in rule:
            comp_list += [x for x in range(rule_set[0], rule_set[1] + 1)]
    comp_list = set(comp_list)

    result, tickets = validate_tickets(tickets_raw=tickets_raw, comp_list=comp_list)
    print(f"Ticket scanning error rate: {result}, Valid tickets: {len(tickets)}")
    return rule_dict, tickets, own_ticket


def puzzle2():
    rule_dict, tickets, own_ticket = puzzle1()

    tickets += own_ticket
    own_ticket = [int(d) for d in own_ticket[0].split(',')]

    ticket_arr = []
    for ticket in tickets:
        ticket_arr.append([int(d) for d in ticket.split(',')])
    ticket_arr = np.array(ticket_arr)

    field_dict = {}
    for i, column in enumerate(ticket_arr.T):
        possible_fields = []
        for key, rule in rule_dict.items():
            lower = rule[0]
            upper = rule[1]
            if all(lower[0] <= value <= lower[1] or upper[0] <= value <= upper[1] for value in column):
                possible_fields.append(key)
        field_dict[i] = possible_fields

    id_list = []
    field_list = []
    while field_dict.keys():
        temp = field_dict.copy()
        for id, field in temp.items():
            if len(field) == 1:
                id_list.append(id)
                field_list.append(field[0])
                field_dict.pop(id)
            for name in field:
                if name in field_list:
                    field.remove(name)
    field_dict = dict(zip(field_list, id_list))

    temp = []
    for key, column in field_dict.items():
        if key.startswith("departure "):
            temp.append(own_ticket[column])

    print(f"Product of 'departure' fields: {reduce(lambda x, y: x * y, temp)}")
    return field_dict


if __name__ == '__main__':
    a = puzzle2()
