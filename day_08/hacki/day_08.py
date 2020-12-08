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
    print(cmds[ind])
    return {
        'accumulator':acc,
        'current_index':ind,
        'cmds':cmds
    }

def part_a(command_ls, input_ls):

    commands = [
        [i, j] for i, j in zip(command_list, command_input)
    ]

    accumulator = 0
    execute_index = 0
    execute_index_new =[]

    while execute_index not in execute_index_new:

        execute_index_new.append(execute_index)
        script_ = script_run(acc=accumulator,ind=execute_index,cmds=commands)
        accumulator, execute_index = script_['accumulator'], script_['current_index']

    return accumulator

def reverse_ls(ls):
    reverse_ls = [i for i in reversed(command_list)]
    return reverse_ls

f_name = 'test_puzzle'

#f_name = 'puzzle_input'

in_ls = misc.load_input_to_list(f_name)

in_ls = [
    i.split(r' ') for i in in_ls
]
command_list = [
    i[0] for i in in_ls
]
command_input = [
    int(re.sub(r'[+]','',i[1])) for i in in_ls
]

def part_b(command_ls, input_ls):
    import random

    accumulator = 0
    execute_index = 0
    execute_index_new = [0]

    while max(execute_index_new) < len(command_ls)-1:
        execute_index_new.append(execute_index)
        if execute_index > len(command_ls)-1:
            break
        elif execute_index == len(command_ls)-1:
            print('hurra')
            break
        i = random.randint(0, len(command_ls)-1)
        if command_ls[i] == 'nop':
            command_ls[i] = 'jmp'
        if command_ls[i] == 'jmp':
            command_ls[i] = 'nop'
        commands = [
            [i, j] for i, j in zip(command_list, command_input)
        ]
        script_ = script_run(acc=accumulator, ind=execute_index, cmds=commands)
        execute_index = script_['current_index']


    return

a = part_b(
    command_ls = command_list,
    input_ls = command_input,
)

print(a)



