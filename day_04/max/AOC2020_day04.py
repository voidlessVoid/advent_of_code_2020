#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "redTribune"
__version__ = "1.0"
__license__ = "MIT"

# This code was created for the 'Advent Of Code' advent challenge 2020. Please feel free to use or modify it.
# I can NOT in any way guarantee that it is doing what it was supposed to do. Or even running... XD

def checkVal(pssprtList):
    
    cnt = 0
    for pssprt in pssprtList:
        val = list(pssprtList[pssprt].keys())
        if "byr" in val and "iyr" in val and "eyr" in val and "hgt" in val and "hcl" in val and "ecl" in val and "pid" in val:
            cnt += 1
        
    return cnt

def checkVal2(pssprtList):
    def consCck(pssprt):
        try:
            if int(pssprt["byr"]) > 2002 or int(pssprt["byr"]) < 1920: return False
            if int(pssprt["iyr"]) > 2020 or int(pssprt["iyr"]) < 2010: return False
            if int(pssprt["eyr"]) > 2030 or int(pssprt["eyr"]) < 2020: return False
            if pssprt["hgt"][-2:] in ["cm", "in"]:
                if pssprt["hgt"][-2:] == "cm":
                    if int(pssprt["hgt"][:-2]) > 193 or int(pssprt["hgt"][:-2]) < 150: return False
                else:
                    if int(pssprt["hgt"][:-2]) > 76 or int(pssprt["hgt"][:-2]) < 59: return False
            else: return False
            if pssprt["hcl"][0] != "#" or len(pssprt["hcl"][1:]) != 6: return False
            else:
                for idx in pssprt["hcl"][1:]:
                    if idx not in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]: return False
            if pssprt["ecl"] not in ["amb","blu","brn","gry","grn","hzl","oth"]: return False
            if int(pssprt["pid"]) < 0 or len(pssprt["pid"]) != 9: return False
            return True
        
        except: return False
    
    cnt = 0
    for pssprt in pssprtList:
        val = list(pssprtList[pssprt].keys())
        if "byr" in val and "iyr" in val and "eyr" in val and "hgt" in val and "hcl" in val and "ecl" in val and "pid" in val:
            stat = consCck(pssprtList[pssprt])
            if stat: cnt += 1
            
    return cnt

if __name__=="__main__":
    
    inp = dict()
    idx = 0
    pssprt = list()
    inp[idx] = dict()
    with open("input.txt") as getInp:
        for line in getInp:
            l = line.strip("\n")
            if l == "":
                for field in pssprt:
                    entry = field.split(":")
                    inp[idx][entry[0]] = entry[1]
                    
                idx += 1
                inp[idx] = dict()
                pssprt = list()
                continue
            
            tl = l.split(" ")
            for field in tl:
                pssprt.append(field)
            
    for field in pssprt:
        entry = field.split(":")
        inp[idx][entry[0]] = entry[1]
        
    if len(inp[idx]) == 0: del inp[idx]
    

    result1 = checkVal(inp)
    result2 = checkVal2(inp)
    print("Answer Code 1: %s" % (result1))
    print("Answer Code 2: %s" % (result2))