def read_input_lines():
    with open('input_05.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

seats = read_input_lines()


def binary_to_decimal(binary):     
        decimal, i, n = 0, 0, 0
        while(binary != 0): 
            dec = binary % 10
            decimal = decimal + dec * pow(2, i) 
            binary = binary//10
            i += 1
        return(decimal) 


def find_seat():
    seat_ids = []
    for seat in seats:
        row = int(binary_to_decimal(int(seat[:7].replace("F","0").replace("B","1"))))
        column = int(binary_to_decimal(int(seat[7:].replace("L","0").replace("R","1")))) 
        seat_id = int(row*8+column)
        seat_ids.append(int(seat_id))
    highest = max(seat_ids)
    seat_ids.sort()
    #print(seat_ids)
    print ("Highest ID: ",highest)
    for x in range(min(seat_ids),max(seat_ids)):
        if x not in seat_ids:
            my_seat = x
    print("My Seat: ",my_seat)
    
    
    
        
find_seat()
