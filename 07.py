#!/usr/bin/python3
import numpy as np
import math

positions=[]
with open('07_input.txt') as f:
    lines = f.readlines()
    positions = np.array([int(i) for i in lines[0].strip().split(',')])

#part 1
medianPoint=np.median(positions)
fuelUsed=sum(np.abs(positions-medianPoint))
print("Part 1 answer:",fuelUsed)

#part 2
# brute force approach - BAD!!

def fuelUsed(startPos, endPos):
    distance=abs(endPos-startPos)
    return distance*(distance+1)/2

smallestFuel=math.inf
for pos in range(min(positions),max(positions)+1):
    fuelTotal=0
    for crab in positions:
        fuelTotal+=fuelUsed(pos, crab)
    if fuelTotal<smallestFuel:
        smallestFuel=fuelTotal

print("Part 2 answer:",smallestFuel)
