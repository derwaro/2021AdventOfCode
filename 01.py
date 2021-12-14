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

#part 2:
f = open('01_input.txt')
l = []
groupsum = []
increasementingroups = 0

for i in f:
    l.append(int(i))

possiblegroupsofthree = len(l) - 2

for i in range(0,possiblegroupsofthree):
    sumofgroups = l[i] + l[i+1] + l[i+2]
    groupsum.append(sumofgroups)

for i in range(1,len(groupsum)-1):
    if groupsum[i] - groupsum[i+1] > 0:
        increasementingroups += 1

print("increasements in groups: " + str(increasementingroups))

