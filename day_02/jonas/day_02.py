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
        counter = 0
        for x in (data):
            lst = x.split()
            letter = lst[1].replace(":","")
            count = lst[2].count(letter)
            boundaries = lst[0].split("-")
            lower_bound = int(boundaries[0])
            upper_bound = int(boundaries[1])
            if count >=lower_bound and count <= upper_bound:
                counter += 1
            
    print(counter)
    

check(data_list)


def check2(data):
    for i in range(len(data)):
        counter = 0
        for x in (data):
            lst = x.split()
            letter = lst[1].replace(":","")
            def split(word): 
                return [char for char in word]
            password = split(lst[2])
            boundaries = lst[0].split("-")
            pos_1 = int(boundaries[0])-1
            pos_2 = int(boundaries[1])-1
            if letter == password[pos_1] and letter != password[pos_2]:
                counter += 1
            if letter == password[pos_2] and letter != password[pos_1]:
                counter += 1           
    print(counter)
    
    

check2(data_list)
