#!/usr/bin/python3

f = open('02_input.txt')
coordinates = [0,0]
path = []
count = 0


for i in f.readlines():
    path.append(i[:-1]) #-1 to not copy the newline character



for a in path:
    count += 1
    print(count)
    print(a[0], a[-1])
    if a[0] == "f":
        coordinates[0] += int(a[-1])
    elif a[0] == "u":
        coordinates[1] -= int(a[-1])
    elif a[0] == "d":
        coordinates[1] += int(a[-1])

print(coordinates)
print(coordinates[0]*coordinates[1])