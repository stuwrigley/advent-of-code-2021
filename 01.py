#!/usr/bin/python3

numbers=[]

with open('01_input.txt') as f:
    lines = f.readlines()
    for line in lines:
        numbers.append(int(line.strip()))


#part 1
increased=0
decreased=0
for index in range(1,len(numbers)):
    diff = numbers[index]-numbers[index-1]
    if diff<0:
        decreased+=1
    if diff>0:
        increased+=1
print increased


#part 2
increased=0
decreased=0
for index in range(3,len(numbers)):
    diff = sum(numbers[index-3:index]) - sum(numbers[index-4:index-1])
    if diff<0:
        decreased+=1
    if diff>0:
        increased+=1
print increased
