#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "redTribune"
__version__ = "1.0"
__license__ = "MIT"

# This code was created for the 'Advent Of Code' advent challenge 2020. Please feel free to use or modify it.
# I can NOT in any way guarantee that it is doing what it was supposed to do. Or even running... XD

import numpy as np


def eval(code, rows, col, limit=None):
    
    def FRONT(interval):
        if np.sum(interval)%2 != 0: return [interval[0], interval[1] + 1 - (interval[1] - interval[0] + 1)/2 - 1]
        else: return [interval[0], interval[1] - (interval[1] - interval[0])/2]
    
    def BACK(interval):
        if np.sum(interval)%2 != 0: return [interval[1] + 1 - (interval[1] - interval[0] + 1)/2, interval[1]]
        else: return [interval[1] - (interval[1] - interval[0])/2, interval[1]]
    
    def LEFT(interval):
        if np.sum(interval)%2 != 0: return [interval[0], interval[1] + 1 - (interval[1] - interval[0] + 1)/2 - 1]
        else: return [interval[0], interval[1] - (interval[1] - interval[0])/2]
    
    def RIGHT(interval):
        if np.sum(interval)%2 != 0: return [interval[1] + 1 - (interval[1] - interval[0] + 1)/2, interval[1]]
        else: return [interval[1] - (interval[1] - interval[0])/2, interval[1]]
    
    lines = [0, rows]
    seats = [0, col]
    for idx in range(7):
        if code[idx].upper() == "F": lines = FRONT(lines)
        elif code[idx].upper() == "B": lines = BACK(lines)
        else: raise ValueError
        if limit != None:
            if col + lines[1] * 8 < limit: return None
        
    line = lines[1]
    for idx in range(3):
        if code[idx + 7].upper() == "R": seats = RIGHT(seats)
        elif code[idx + 7].upper() == "L": seats = LEFT(seats)
        else: raise ValueError
        if limit != None:
            if line * 8 + seats[1] < limit: return None
        
    seat = seats[1]
    return [int(line), int(seat)]
             
if __name__=="__main__":
    plane = list()
    with open("input.txt") as getInp:
        for line in getInp: plane.append(line.strip())
    
    pssngrID = list()               
    planeMap = np.array([])
    for idx in range(128): planeMap = np.concatenate((planeMap, np.arange(8)), axis=0)
     
    planeMap = planeMap.reshape(128,8) 
       
    for pssngr in plane:
        val = eval(pssngr, 127, 7)
        pssngrID.append(val[0] * 8 + val[1])
        planeMap[val[0],val[1]] = -1
    
    maxID = np.max(pssngrID)
    mySeat = np.where(planeMap != -1)  
    mySeatLine = mySeat[0]
    seatID = list()
    for idx, line in enumerate(mySeatLine): seatID.append(mySeat[0][idx] * 8 + mySeat[1][idx])
        
    for idx, element in enumerate(seatID):
        if idx == 0 or idx == len(seatID) - 1: continue
        if element != seatID[idx - 1] + 1 and element != seatID[idx + 1] - 1:
            mySeatID = seatID[idx]
            break
    
    result = "Answer 1: " + str(maxID) + "\tAnswer 2: " + str(mySeatID)
    print("Answer Code: %s" % (result))