#!/usr/bin/python3


f = open('03_input.txt')

input_bin = [line[:-1] for line in f.readlines()]
input_formatted = [[],[],[],[],[],[],[],[],[],[],[],[]]
counter = 0
gamma = ""
epsilon = ""

#get first position from line in input into a list
for i in range(0,12):
    for a in input_bin:
        input_formatted[i].append(a[i])

for i in input_formatted:
    a = max(set(i), key = i.count) #get maximum occurence of number
    b = min(set(i), key = i.count) #get minimum occurence of number
    gamma += a
    epsilon += b

print(int(gamma, 2)*int(epsilon, 2))