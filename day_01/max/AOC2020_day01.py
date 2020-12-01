#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "redTribune"
__version__ = "1"
__license__ = "MIT"

# This code was created for the 'Advent Of Code' advent challenge 2020. Please feel free to use or modify it.
# I can NOT in any way guarantee that it is doing what it was supposed to do. Or even running... XD

from copy import deepcopy

def searchSum():
    for idx, numSum in enumerate(testSum):
        for numInp in inp:
            if numSum + numInp == 2020: return numInp * numSum
            
        del inp[0]

if __name__=="__main__":
    
    inp = list()
    with open("input.txt") as getInp:
        for line in getInp:
            inp.append(int(line))
                   
    testSum = deepcopy(inp)
    result = searchSum()
    
    print("Answer Code: %s" % (result))