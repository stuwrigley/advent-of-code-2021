#!/usr/bin/python3

operations=[]

with open('02_input.txt') as f:
    lines = f.readlines()
    for line in lines:
        operations.append(line.strip())

#part 1
depth=0
horizontal=0
for op in operations:
    op_components = op.split()
    if op_components[0]=="forward":
        horizontal+=int(op_components[1])
    if op_components[0]=="down":
        depth+=int(op_components[1])
    if op_components[0]=="up":
        depth-=int(op_components[1])
print("Part 1 answer:",horizontal*depth)

#part 2
aim=0
depth=0
horizontal=0
for op in operations:
    op_components = op.split()
    if op_components[0]=="forward":
        horizontal+=int(op_components[1])
        depth+=aim*int(op_components[1])
    if op_components[0]=="down":
        aim+=int(op_components[1])
    if op_components[0]=="up":
        aim-=int(op_components[1])
print("Part 2 answer:",horizontal*depth)
