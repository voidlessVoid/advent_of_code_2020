lst = []
lst2020 = []
lst2020_2 = []

with open("input_day1") as f:
    lines = f.readlines()
    for line in lines:
        line = int(line)
        lst.append(line)
        difference = 2020 - line
        lst2020.append(difference)
lst2020_2 = lst
for element in lst:
    for element1 in lst2020_2:
        sum1 = element + element1
        difference2 = 2020 - sum1
        if difference2 in lst:
            print element
            print element1
            print difference2
            product = element * element1 * difference2
            print product
            print 
