# o7 CMDRS

from misc_hacki import misc

from collections import ChainMap
import numpy as np
import re

#f_name = 'test_puzzle'
f_name = 'puzzle_input'
in_ls = misc.load_input_to_list(f_name)
bag_to_find = "shinygold"

rule_set = [[j.split(', ') for j in i.split(' contain ')] for i in in_ls]
index_level_1, bags = [i[0] for i in rule_set], [i[1:] for i in rule_set]
index_level_1, bags = [[item for sublist in i for item in sublist] for i in [index_level_1,bags]]

#### exceptionally ugly ####
count = [[map(int, re.findall(r"\d", j)) for j in i]for i in bags]

c = []
for i in count:
    c.append([int(item) for sublist in i for item in sublist])
c_new = []
for j in c:
    if j == []:
        j = [np.nan]
    c_new.append(j)

#### exceptionally ugly ####

index_level_1 = [re.sub(r"[ ]|[.]|bag.", '', i) for i in index_level_1]
bags = [[re.sub(r"[ ]|[.]|bag.|bag|\d", '', j) for j in i] for i in bags]

bag_dict = dict(zip(index_level_1,zip(bags, c_new)))

def puzzle1():
    parent_bags = ['shinygold']
    def __color_update(in_color_list):
        parent_bags = []
        for color in in_color_list:
            for k, v in bag_dict.items():
                if color in v[0]:
                    parent_bags.append(k)
        return list(set(parent_bags))

    color_counter_list = []
    while parent_bags:
        parent_bags = __color_update(parent_bags)
        color_counter_list += parent_bags

    print(len(set(color_counter_list)))

def puzzle2():

    daughter_bags = [['shinygold',1,1]]

    def __color_update(in_color_list):
        counter = 0
        daughter_bags_new = []
        for color in in_color_list:
            for k, l in zip(*bag_dict[color[0]]):
                if k != "noother":
                    daughter_bags_new.append([k,l,l*color[2]])
                    counter+=l*color[2]
        return daughter_bags_new, counter

    counter=0
    while daughter_bags:
        daughter_bags,count = __color_update(daughter_bags)
        counter+=count
        print(daughter_bags,counter)
if __name__ == '__main__':
    puzzle1()
    puzzle2()