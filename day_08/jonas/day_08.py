def read_input_lines():
    with open('input_08.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

boot = read_input_lines()
boot_sep = []
for x in boot:
	a = x.split()
	boot_sep.append(a)


nop = "nop"
acc = "acc"
jmp = "jmp"


def part_a():

	position = 0
	accumulator = 0
	
	tested_steps = []

	 
	while position not in tested_steps:
		x = boot_sep[position]
		if x[0] == nop:
			tested_steps.append(position)
			position += 1
			
		if x[0] == acc :
			accumulator += int(x[1])
			tested_steps.append(position)
			position +=1
			
		if x[0] == jmp:
			tested_steps.append(position)
			position += int(x[1])
			
	print("Accumulator", accumulator)
	#print(tested_steps)

part_a()


	

