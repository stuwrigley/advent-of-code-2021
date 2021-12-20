#!/usr/bin/python3
import numpy as np
from copy import deepcopy as dc

with open('19_input.txt') as f:
    lines = f.readlines()

def parseInput(lines):
    scanners=[]
    for line in lines:
        line=line.strip()
        if line.startswith('--'):
            beacons=[]
        elif line=='':
            scanners.append(beacons)
            beacons=[]
        else:
            beacons.append(tuple(int(i) for i in line.split(',')))
    scanners.append(beacons)
    return scanners

def euclideanDistance(a,b):
    return math.sqrt(math.pow(a[0]-b[0],2) + math.pow(a[1]-b[1],2) + math.pow(a[1]-b[1],2))

def manhattanDistance(a,b):
    return (a[0]-b[0]) + (a[1]-b[1]) + (a[2]-b[2])

def shift(a,b):
    return tuple([a[0]-b[0], a[1]-b[1], a[2]-b[2]])

def rotations(beacons):
    localBeaconList=dc(beacons)
    rotations=[]
    for ind1 in range(4):
        for ind2 in range(4):
            rotations.append(localBeaconList)
            localBeaconList={(z, y, -x) for x, y, z in localBeaconList}
        rotations.append({(y, -x, z) for x, y, z in localBeaconList})
        rotations.append({(-y, x, z) for x, y, z in localBeaconList})
        localBeaconList={(x, z, -y) for x, y, z in localBeaconList}
    return rotations

def overlap(beacons1, beacons2):
    global scannerLocations
    for rotationSet in rotations(beacons2):  # brute force try every possible rotation
        for beacon1 in beacons1:
            for beacon2 in rotationSet:
                offset = shift(beacon2,beacon1)  # find translation needed to make these beacons be located same position
                newPositions=[]
                for beacon2 in rotationSet:    # apply this translation to every beacon
                    newPositions.append(shift(beacon2, offset))
                newPositions=set(newPositions)
                if len(beacons1 & newPositions) >= 12:  # how many translated beacon locations match the master beacon locations?
                    scannerLocations.append(offset)
                    return newPositions



scanners=parseInput(lines)

#part 1
masterSetOfBeacons=set(scanners[0])
otherScanners=scanners[1:]
scannerLocations=[[0,0,0]]
while otherScanners:
    overlappingBeaconsSet=overlap(masterSetOfBeacons,otherScanners[0])
    if overlappingBeaconsSet:
        masterSetOfBeacons=masterSetOfBeacons | overlappingBeaconsSet
        otherScanners.pop(0)
    else:
        otherScanners.append(otherScanners.pop(0))
print("Part 1 answer:",len(masterSetOfBeacons))

#part 2
maxDistance=0
for scanner1Location in scannerLocations:
    for scanner2Location in scannerLocations:
        if scanner1Location==scanner2Location:
            continue
        d=manhattanDistance(scanner1Location,scanner2Location)
        if d>maxDistance:
            maxDistance=d
print("Part 2 answer:",maxDistance)
