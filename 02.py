#!/usr/bin/python3

#part 1
f = open('02_input.txt')
coordinates = [0,0] #forward, depth
path = []
count = 0


for i in f.readlines():
    path.append(i[:-1]) #-1 to not copy the newline character



for a in path:
    if a[0] == "f":
        coordinates[0] += int(a[-1])
    elif a[0] == "u":
        coordinates[1] -= int(a[-1])
    elif a[0] == "d":
        coordinates[1] += int(a[-1])


print(coordinates[0]*coordinates[1])


#part 2

coordinates = [0,0,0] #forward, depth, aim
print(coordinates)

for a in path:
    if a[0] == "f":
        coordinates[0] += int(a[-1])
        coordinates[1] += coordinates[1]*coordinates[2]
    elif a[0] == "u":
        #coordinates[1] -= int(a[-1])
        coordinates[2] -= int(a[-1])
    elif a[0] == "d":
        #coordinates[1] += int(a[-1])
        coordinates[2] += int(a[-1])

print(coordinates)
print(coordinates[0]*coordinates[1])
