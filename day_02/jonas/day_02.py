data_txt = open("input_2.csv")
data_list = []
for line in data_txt:
    stripped_line = line.strip()
    data_list.append(stripped_line)
data_txt.close()
data_list
#print(data_list)

        
def check(data):
    for i in range(len(data)):
        results = []
        for x in (data):
            lst = x.split()
            letter = lst[1].replace(":","")
            count = lst[2].count(letter)
            boundaries = lst[0].split("-")
            lower_bound = int(boundaries[0])
            upper_bound = int(boundaries[1])
            if count >=lower_bound and count <= upper_bound:
                results.append(True)
            else:
                results.append(False)
    print(len(results))
    print(len(data))
    print(results.count(True))
    

check(data_list)