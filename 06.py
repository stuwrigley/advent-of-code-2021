#!/usr/bin/python3
import numpy as np

maxAge=8
ageTotals=[0,0,0,0,0,0,0,0,0] #total number of fish with age 0, 1, ..., 8

with open('06_input.txt') as f:
    lines = f.readlines()
    allFishAges = np.array([int(i) for i in lines[0].strip().split(',')])
    for age in range(maxAge+1):
        ageTotals[age]=sum(allFishAges==age)

def runSimulation(ageTotals,numDays):
    for day in range(numDays):
        newTotals=[0,0,0,0,0,0,0,0,0]
        newTotals[0:8]=ageTotals[1:9]
        newTotals[8]=ageTotals[0]
        newTotals[6]+=ageTotals[0]
        ageTotals=newTotals.copy()
    return ageTotals

print("Part 1 answer:",sum(runSimulation(ageTotals,80)))
print("Part 2 answer:",sum(runSimulation(ageTotals,256)))
