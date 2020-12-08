from misc_hacki import misc
import numpy as np
import re


def script_run(acc, ind, cmds):
    index_out = ind
    if cmds[ind][0] == 'nop':
        index_out += 1
    if cmds[ind][0] == 'acc':
        acc += cmds[ind][1]
        index_out += 1
    if cmds[ind][0] == 'jmp':
        index_out += cmds[ind][1]
    return {
        'accumulator': acc,
        'current_index': index_out,
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

f_name = 'puzzle_input'

# f_name = 'test_puzzle'

def get_index(f_name):
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
        indeces = []
        for i, j in enumerate(command_list):
            if j == 'jmp' or j == 'nop':
                indeces.append(i)

        ran = random.randint(0, len(indeces)-1)
        if execute_index > len(command_list)-1:
            break

        if command_list[indeces[ran]] == 'nop':
            command_list[indeces[ran]] = 'jmp'
        if command_list[indeces[ran]] == 'jmp':
            command_list[indeces[ran]] = 'nop'



        #print(ran)
        commands = [
            [i, j] for i, j in zip(command_list, command_input)
        ]

        script_ = script_run(
                acc=accumulator,
                ind=execute_index,
                cmds=commands
                )
        execute_index = script_['current_index']
        if execute_index == len(command_list)-1 :

            print('hurra', indeces[ran], command_list)

    return accumulator, command_list


a = part_a(
    f_name
)
b = get_index(
    f_name
)

print(b)
