def read_input_lines():
    with open('input_3.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]
data = read_input_lines()

##So this apparently works after i implemented the idea from Hacki, i realized to create a list of numbers first to take the individual rows from

lst_of_rows= []
start = 0
for x in data:
    lst_of_rows.append(start)
    start += 1
#print(lst_of_rows)

position=0
counter = 0

for lst in lst_of_rows:
    row = data[lst]
    if position > (len(row)-1):
        position -= (len(row))
    if row[position] == "#":
        counter +=1
    position += 3
    
print(counter)



######### NEED SOME ADVISE ON THIS ONE#########
#My way until i gave up was looking somewhat like this and i still do not understand why the above works and the following not. 
#Why is the "position" variable changing outside the loop in the above, but does stop at 30 and in the following? This was driving me mad and i still dont really get the difference.


position = 0
counter = 0

for each_list in data:
    waypoint = each_list[position]
    #print(waypoint)
    #print (position)
    if position > 30:
        position -= 30
    if waypoint == "#":
        counter += 1
    position += 3

print(counter)

