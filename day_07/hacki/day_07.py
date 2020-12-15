# o7 CMDRS

from misc_hacki import misc
import pandas as pd
from collections import ChainMap
import numpy as np
import re


f_name = 'test_puzzle'
#f_name = 'puzzle_input'
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


parent_bags = []

for key in bag_dict.keys():
    #print(key, bag_dict[key])
    for col, con in zip(bag_dict[key][0],bag_dict[key][1]):
        if col == bag_to_find:
           parent_bags.append({key: con})

parent_bags = dict(ChainMap(*parent_bags))
b_count = []
for key in bag_dict.keys():
    #print(key, bag_dict[key])
    for co in zip(bag_dict[key][0]):
        b_count.append(set(co)&set(parent_bags.keys()))

b_count = [b for b in b_count if b]
print(b_count)
