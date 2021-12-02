#!/usr/bin/python3

f = open('01_input.txt')

inputlist = [[i, int(e)] for i, e in enumerate(f)]

increases = 0
decreases = 0
nextinput = 0

for x in inputlist:    
    if x[0] != 0:
        if inputlist[nextinput][1] < x[1]:
            print(str(x[1]) + " increased")
            increases += 1
            nextinput += 1
        else:
            print(str(x[1]) + " decreased")
            decreases += 1
            nextinput += 1
    else:
        print(str(x[1]) + " N/A")

print("increases: " + str(increases))
print("decreases: " + str(decreases))