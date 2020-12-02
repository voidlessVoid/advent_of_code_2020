#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "redTribune"
__version__ = "0.1"
__license__ = "MIT"

# This code was created for the 'Advent Of Code' advent challenge 2020. Please feel free to use or modify it.
# I can NOT in any way guarantee that it is doing what it was supposed to do. Or even running... XD

import numpy as np
import csv
from copy import deepcopy
import re

def POLICY1(inp):
    val_cnt = 0
            
    for passwd in inp:
        pol = re.findall(r"\w+", inp[passwd])
        pol_min = int(pol[0])
        pol_max = int(pol[1])
        pol_target = pol[2]
        passwd_cnt = passwd.count(pol_target)
        if passwd_cnt >= pol_min and passwd_cnt <= pol_max: val_cnt +=1
        
    return val_cnt

def POLICY2(inp):
    val_cnt = 0
            
    for passwd in inp:
        pol = re.findall(r"\w+", inp[passwd])
        pol_min = int(pol[0]) - 1
        pol_max = int(pol[1]) - 1
        pol_target = pol[2]
        if passwd[pol_min] == pol_target or passwd[pol_max] == pol_target:
            if passwd[pol_min] == pol_target and passwd[pol_max] == pol_target: continue
            else: val_cnt +=1
        
    return val_cnt
    

if __name__=="__main__":
    
    inp = dict()
    with open("input.txt") as getInp:
        for line in getInp:
            l = line.strip().split(": ")
            inp[l[1]] = l[0]
            
    val_cnt1 = POLICY1(inp)
    val_cnt2 = POLICY2(inp)

    
    result = str(val_cnt1) + " and " +  str(val_cnt2)
    print("Answer Code: %s" % (result))