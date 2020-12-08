from misc_hacki import misc
import re


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
    int(
        re.sub(r'[+]',
               '',
               i[1]
               )
    ) for i in in_ls
]

command_ls = []
for i,j in zip(
        command_list,
        command_input
):
    command_ls.append(
        [i , j]
    )


def execute(commands):

    count = 0
    execute_index = 0
    execute_index_new =[]

    while execute_index not in execute_index_new:

        execute_index_new.append(execute_index)
        if commands[execute_index][0] == 'nop':
            execute_index +=1
        if commands[execute_index][0] == 'acc':
            count += commands[execute_index][1]
            execute_index += 1
        if commands[execute_index][0] == 'jmp':
            execute_index += commands[execute_index][1]

    return count

e = execute(command_ls)

print(e, command_ls)