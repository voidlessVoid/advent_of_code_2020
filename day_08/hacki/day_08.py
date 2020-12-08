from misc_hacki import misc
import numpy as np
import re


def script_run(acc, ind, cmds):
    if cmds[ind][0] == 'nop':
        ind += 1
    if cmds[ind][0] == 'acc':
        acc += cmds[ind][1]
        ind += 1
    if cmds[ind][0] == 'jmp':
        ind += cmds[ind][1]

    return {
        'accumulator': acc,
        'current_index': ind,
    }


def part_a(f_name):

    in_ls = misc.load_input_to_list(f_name)

    in_ls = [
        i.split(r' ') for i in in_ls
    ]
    command_list = [
        i[0] for i in in_ls
    ]
    command_input = [
        int(re.sub(r'[+]', '', i[1])) for i in in_ls
    ]

    commands = [
        [i, j] for i, j in zip(command_list, command_input)
    ]
    accumulator = 0
    execute_index = 0
    execute_index_new = []

    while execute_index not in execute_index_new:
        execute_index_new.append(execute_index)
        script_ = script_run(
            acc=accumulator,
            ind=execute_index,
            cmds=commands
        )
        accumulator, execute_index = script_['accumulator'], script_['current_index']

    return accumulator

# f_name = 'puzzle_input'

f_name = 'test_puzzle'

def part_b(f_name):
    import random

    accumulator = 0
    execute_index = 0

    while True:
        in_ls = misc.load_input_to_list(f_name)
        in_ls = [
            i.split(r' ') for i in in_ls
        ]
        command_list = [
            i[0] for i in in_ls
        ]
        command_input = [
            int(re.sub(r'[+]', '', i[1])) for i in in_ls
        ]

        ran = random.randint(0, len(command_list) - 1)
        if execute_index > len(command_list) - 1:
            break
        elif execute_index == len(command_list) - 1:
            print('hurra')
            break

        if command_list[ran] == 'nop':
            command_list[ran] = 'jmp'
            print(ran, command_list[ran])
        if command_list[ran] == 'jmp':
            command_list[ran] = 'nop'
            print(ran, command_list[ran])
        commands = [
            [i, j] for i, j in zip(command_list, command_input)
        ]
        script_ = script_run(
                acc=accumulator,
                ind=execute_index,
                cmds=commands
                )
        execute_index = script_['current_index']

    return


a = part_a(
    f_name
)
b = part_b(
    f_name
)

print(b)
