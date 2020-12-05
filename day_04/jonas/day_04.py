def input():
    with open('input_04.txt', 'r') as file:
        return file.read().strip()
list_of_passports = input().split("\n\n")

def part_a():
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
                                    counter += 1
    print(counter)



part_a()


#print(list_of_passports[:2])


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
                                    #check for len(pid)...
                                    
                                        #try eye_color with " if ey_color is blue or green"
                                    
                                            #check for height 
                                                #if hgt in x:
                                                    #hgt_position = x.find(hgt)
                                                    #inch = "in"
                                                    #cm = "cm"
                                                    #height_start = x[hgt_position:]
                                                    #height_string = height_start[:10]
                                                    #if inch in height_string:

                                                        #try using regex for hex color codes eye colors?
                                                            counter_2 += 1
    print(counter_2)

part_b()
            
        
