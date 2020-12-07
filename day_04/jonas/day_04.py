def input():
    with open('input_04.txt', 'r') as file:
        return file.read().strip()
list_of_passports = input().split("\n\n")
new_list_filtered = []
def count_valids():
    counter = 0
    
    byr = "byr"
    iyr = "iyr"
    eyr = "eyr"
    hgt = "hgt"
    hcl = "hcl"
    ecl = "ecl"
    pid = "pid"
    
    for x in list_of_passports:
        if byr in x:
            if iyr in x:
                if eyr in x:
                    if hgt in x:
                        if hcl in x:
                            if ecl in x:
                                if pid in x:
                                    new_list_filtered.append(x)
                                    counter += 1
    print(counter)



count_valids()


#print(list_of_passports[:2])

import re
def part_b():
    counter_2 = 0
    byr = "byr"
    iyr = "iyr"
    eyr = "eyr"
    hgt = "hgt"
    hcl = "hcl"
    ecl = "ecl"
    pid = "pid"
    for x in list_of_passports:
        if byr in x:
            byr_position = x.find(byr)
            birth_year_start = x[byr_position+4:]
            birth_year = int(birth_year_start[:4])
            if birth_year >= 1920 and birth_year <= 2002:
                if iyr in x:
                    iyr_position = x.find(iyr)
                    issue_year_start = x[iyr_position+4:]
                    issue_year = int(issue_year_start[:4])
                    if issue_year >= 2010 and issue_year <= 2020:
                        if eyr in x:
                            eyr_position = x.find(eyr)
                            expiration_year_start = x[eyr_position+4:]
                            expiration_year = int(expiration_year_start[:4])
                            if expiration_year >= 2020 and expiration_year <= 2030:
                                if pid in x:
                                    pid_position = x.find(pid)
                                    pass_id_start = x[pid_position+4:]
                                    pass_id = pass_id_start[:9]
                                    if sum(n.isdigit() for n in pass_id_start[:10]) == 9:
                                        length = sum(c.isdigit() for c in pass_id)
                                        if length == 9:                                                    
                                            if ecl in x:
                                                colors = ["amb","blu","brn","gry","grn","hzl","oth"]
                                                ecl_position = x.find(ecl)
                                                eye_color_start = x[ecl_position+4:]
                                                eye_color = eye_color_start[:3]
                                                if eye_color in colors:
                                                    if hcl in x:
                                                        hcl_position = x.find(hcl)
                                                        hair_color_start = x[hcl_position+4:]
                                                        hair_color = hair_color_start[:7]
                                                        hcl_validation = bool(re.match(r"^#[0-9a-f]{6}$", hair_color))
                                                        if hcl_validation == True:
                                                            if hgt in x:
                                                                inch = "in"
                                                                cm = "cm"
                                                                hgt_position = x.find(hgt)
                                                                height_start = x[hgt_position+4:]
                                                                height_var = (height_start[:3])
                                                                if inch in height_start:
                                                                    height_var_inch = int(height_var[:-1])
                                                                    if height_var_inch >= 59 and height_var_inch <= 76:
                                                                        counter_2+=1            
                                                                if cm in height_start: 
                                                                    if len(re.findall('\\d',height_var)) == 3:
                                                                    #print(height_var)\n"
                                                                        if int(height_var) >= 150 and int(height_var) <=193:
                                                                            counter_2 += 1
                                                            
                                    
    print("valid passports",counter_2)

                                      

part_b()
            
        
