#!/usr/bin/python3
import numpy as np

with open('22_input.txt') as f:
    lines = f.readlines()

def parseSingleLine(line,minPos,maxPos):
    onOrOff,data=line.strip().split()
    data=data.split(',')
    minX,maxX=[int(i) for i in (data[0].split('='))[1].split('..')]
    minY,maxY=[int(i) for i in (data[1].split('='))[1].split('..')]
    minZ,maxZ=[int(i) for i in (data[2].split('='))[1].split('..')]
    minX=max(minPos,minX)
    minY=max(minPos,minY)
    minZ=max(minPos,minZ)
    maxX=min(maxPos,maxX)
    maxY=min(maxPos,maxY)
    maxZ=min(maxPos,maxZ)
    return onOrOff,minX,maxX,minY,maxY,minZ,maxZ

def parseInput(lines,minPos,maxPos):
    output=[]
    for line in lines:
        output.append(parseSingleLine(line,minPos,maxPos))
    return output


#part 1
minPos=-50
maxPos=50
input=parseInput(lines,minPos,maxPos)

reactorCore=set()
for step in input:
    for xPos in range(step[1],step[2]+1):
        for yPos in range(step[3],step[4]+1):
            for zPos in range(step[5],step[6]+1):
                if step[0]=='on':
                    reactorCore.add((xPos,yPos,zPos))
                else:
                    if (xPos,yPos,zPos) in reactorCore:
                        reactorCore.remove((xPos,yPos,zPos))

print("Part 1 answer:",len(reactorCore))

#part 2
print("Part 2 answer:")
