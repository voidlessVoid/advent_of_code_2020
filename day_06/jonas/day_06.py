import string


def input():
    with open('input_06.txt', 'r') as file:
        return file.read().strip()

answers = input().split("\n\n")
abc = list(string.ascii_lowercase)

def part_a():
	result_list = []
	for answer in answers:
		answer_ordered = answer.replace("\n","")
		result = 0
		for char in abc:
			if char in answer_ordered:
				result +=1
		result_list.append(result)
	print("part a sum: ",sum(result_list))

part_a()

answers_astyle = []
for answer in answers:
	answer_ordered = answer.replace("\n","")
	answers_astyle.append(answer_ordered)
 
answers_bstyle = []
for answer in answers:
	answers_bstyle.append(answer.split("\n"))



def part_b():
	final_list= []
	for i in range(len(answers_astyle)):
		results = []
		count = 0
		for char in abc:
			occ = answers_astyle[i].count(char)
			if occ == len(answers_bstyle[i]):
				count += 1
				results.append(1)
		each_sum = sum(results)
		final_list.append(each_sum)
	print("final sum: ",sum(final_list))
			
	

part_b()
