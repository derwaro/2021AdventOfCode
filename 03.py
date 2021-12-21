#!/usr/bin/python3


f = open('03_input.txt')

input = [line[:-1] for line in f.readlines()]
input_formatted = [[],[],[],[],[],[],[],[],[],[],[],[]]
counter = 0

for i in input:
    for a in i:
        if counter < 7:
            input_formatted[counter] = a
            counter += 1
        else:
            counter = 0


