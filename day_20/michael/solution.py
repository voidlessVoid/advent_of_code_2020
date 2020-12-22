import os
import operator
from collections import  defaultdict
from functools import reduce

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


interfaceFuncs = [
    lambda y: y[0], # upper
    lambda y:  "".join([x[0] for x in y]), # left
    lambda y: y[-1], # lower
    lambda y:  "".join([x[-1] for x in y]), # right
]


def parse():
    tiles = [x.split("\n") for x in read_input_text().split("\n\n")]
    tileNr2Interfaces = {}
    interfaces2tileNr = defaultdict(list)
    tile2Content = {}
    for tile in tiles:
        tileName = int(tile[0].split()[-1][:-1])
        tileContent = tile[1:]
        interfaces = [f(tileContent) for f in interfaceFuncs]
        interfaces_stand = [min([x,x[::-1]]) for x in interfaces]
        tileNr2Interfaces[tileName] = interfaces_stand
        tile2Content[tileName] = tileContent

        for interface in interfaces_stand:
            interfaces2tileNr[interface].append(tileName)

    return tile2Content, tileNr2Interfaces, interfaces2tileNr


def part_a():
    tile2Content, tileNr2Interfaces, interfaces2tileNr = parse()
    corners = [k for k,i in tileNr2Interfaces.items() if len([connection for connection in i if len(interfaces2tileNr[connection]) > 1]) == 2]
    print(reduce(operator.mul, corners))

def rotate90(tilecontent):
    return ["".join([tilecontent[x][-y] for x in range(len(tilecontent))]) for y in range(1,len(tilecontent[0])+1)]

def get8options(tilecontent):
    for __ in range(2):
        for _ in range(4):
            tilecontent = rotate90(tilecontent)
            yield tilecontent

        tilecontent = tilecontent[::-1] # flip


def isValid(loc, content, solution,tile2Content):
    for adj, facing in [(loc + delta, facing) for facing, delta in enumerate([-1, -1j, 1, 1j]) if
                        loc + delta in solution]:
        if (interfaceFuncs[(facing+2)%4](tile2Content[solution[adj]])) != (interfaceFuncs[facing](content)):
            break
    else:
        return True

def getAdjacent(solution,interfaces2tileNr,tile2Content, loc):
    output = set()
    for facing, delta in enumerate([-1, -1j, 1, 1j]):
        adjloc = loc + delta
        if adjloc not in solution:
            facingMargin =interfaceFuncs[facing](tile2Content[solution[loc]])
            facingMarginNormalised = min([facingMargin,facingMargin[::-1]])
            counterparts = set(interfaces2tileNr[facingMarginNormalised]) - {solution[loc]}
            if counterparts :
                assert len(counterparts) == 1
                output.add((adjloc,counterparts.pop()))
    return output

def part_b():

    tile2Content, tileNr2Interfaces, interfaces2tileNr = parse()

    starttile = list(tile2Content.keys())[0]
    solution = {0:starttile}
    current = {0}

    while current:
        nextVisit = set()
        for loc in current:
            nextVisit|= getAdjacent(solution,interfaces2tileNr,tile2Content, loc)

        for loc, tileNr in nextVisit:
            tileContents = get8options(tile2Content[tileNr])
            for option in tileContents:
                if isValid(loc, option, solution, tile2Content):
                    solution[loc] = tileNr
                    tile2Content[tileNr] = option
                    break
            else:
                assert False

        current = set(x[0] for x in nextVisit)

    dragonstrings =[x for x in
     """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split("\n")]
    dragondeltas = {(row,col) for row in range(len(dragonstrings))
                              for col in range(len(dragonstrings[row]) )
                              if dragonstrings[row][col] == "#"} #compared to upper left


    def findDragons(grid):
        allHashTagLocs = {(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if
                          grid[row][col] == "#"}
        foundDragons = {(row,col) for row in range(len(grid)) for col in range(len(grid[0]))
                        if all([(row + delta[0], col+delta[1]) in allHashTagLocs for delta in dragondeltas])}
        return foundDragons


    minrow, maxrow = min(x.real for x in solution),  max(x.real for x in solution)
    mincol, maxcol = int(min(x.imag for x in solution)), int(max(x.imag for x in solution))

    merged = []
    for tilerow in range(minrow,maxrow+1):
        for vpixel in range(1,9) :
            newRow = []
            for tilecol in range(mincol,maxcol+1):
                for hpixel in range(1,9):
                    newRow.append(tile2Content[solution[tilerow + 1j * tilecol]][vpixel][hpixel])
            merged.append("".join(newRow))

    for rotation in get8options(merged):
        founddragons = findDragons(rotation)
        if founddragons:
            alldragonLocs = {(founddragon[0]+delta[0],founddragon[1]+delta[1] ) for founddragon in founddragons for delta in dragondeltas}
            allHashTagLocs = {(row,col) for row in range(len(rotation)) for col in range(len(rotation[0])) if rotation[row][col] == "#"}
            print(len(allHashTagLocs-alldragonLocs))

part_b()

