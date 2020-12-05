import re

in_file = "input.txt"


def load_input(file):
    with open(file, 'r') as f:
        in_list = [line.rstrip('\n') for line in f]
    return in_list

def seat_id(row,column):
    return row * 8 + column

def scan_boardingpass(passcode):
    row=range(0,127)
    column = range(0, 7)

    for char in passcode:
        if char == "F": # lower half
            row=row[0:(len(row)) // 2]
        if char == "B":# upper half
            row =row[(len(row)+1)//2:]
        if char== "L":# lower half
            column= column[0:(len(column)) // 2]
        if char== "R":# upper half
            column = column[(len(column)+1)//2:]
    seat_ID= seat_id(row.stop,column.stop)

    return row.stop,column.stop,seat_ID


def puzzle1():
    in_list=load_input(in_file)
    Seat=(0,0,0)
    seat_plan = []
    for boardingpass in in_list:
        pass_seat=scan_boardingpass(boardingpass)
        if pass_seat[2] > Seat[2]:
            Seat=(pass_seat)
        seat_plan.append(pass_seat)
    print(f"Highest Seat: R{Seat[0]} C{Seat[1]} SeatID: {Seat[2]}")
    return seat_plan

def puzzle2(occupied_seats):
    plan = [[c for c in range(0, 7)] for r in range(0, 127)]
    for n in occupied_seats:
        if plan[n[0]] is not []:
            if n[1] in plan[n[0]]:
                plan[n[0]].remove(n[1])
    for i,column in enumerate(plan):
        if len(column)==1:
            print(f"Own seat ID is: {seat_id(i, column[0])}")

if __name__ == '__main__':
    seat_list=puzzle1()
    puzzle2(seat_list)