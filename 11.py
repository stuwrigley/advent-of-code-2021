#!/usr/bin/python3
import numpy as np
import math

with open('11_input.txt') as f:
    lines = f.readlines()

numRows=len(lines)
numCols=len(lines[0].strip())
energies=np.zeros((numRows,numCols))
for rowNum in range(numRows):
    energies[rowNum]=(np.array([int(i) for i in lines[rowNum].strip()]))

numSteps=100

def neighbouringLocations(loc,numRows,numCols):
    neighbours=[]
    for row in range(max(0,loc[0]-1),min(numRows,loc[0]+2)):
        for col in range(max(0,loc[1]-1),min(numCols,loc[1]+2)):
            thisLoc=((row,col))
            if thisLoc!=loc:
                neighbours.append(((row,col)))
    return neighbours

def processFlash(energies,flashLocation):
    energies[flashLocation]+=1
    neighbours=neighbouringLocations(flashLocation,numRows,numCols)
    for neighbour in neighbours:
        energies[neighbour]+=1

def runOneStep(energies):
    energies=energies+1

    flashes=np.where(energies > 9)
    newFlashLocations=set([((i,j)) for i,j in zip(flashes[0], flashes[1])])
    oldFlashLocations=set()

    while len(newFlashLocations)>0: # at least one has flashed
        for flashLocation in newFlashLocations:
            processFlash(energies,flashLocation)

        oldFlashLocations=oldFlashLocations.union(newFlashLocations)
        flashes=np.where(energies > 9)
        curFlashLocations=set([((i,j)) for i,j in zip(flashes[0], flashes[1])])

        newFlashLocations=curFlashLocations.difference(oldFlashLocations)

    numFlashes=len(np.where(energies > 9)[0])
    energies[energies>9]=0
    return energies,numFlashes


#part 1
numFlashes=0
for step in range(numSteps):
    energies,flashes=runOneStep(energies)
    numFlashes+=flashes
print("Part 1 answer:",numFlashes)


#part 2
for rowNum in range(numRows):
    energies[rowNum]=(np.array([int(i) for i in lines[rowNum].strip()]))
step=0
while(True):
    energies,flashes=runOneStep(energies)
    step+=1
    if sum(sum(energies))==0:
        break
print("Part 2 answer:",step)
