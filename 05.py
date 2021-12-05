#!/usr/bin/python3
import numpy as np

def addHorizontalAndVerticalLines(startX,startY,endX,endY,map):
    map[min(startX,endX):max(startX,endX)+1,min(startY,endY):max(startY,endY)+1]+=1
    return map

def addDiagonalLines(startX,startY,endX,endY,map):
    lineLength=np.abs(endX-startX)  # assuming they're all the same length
    xDirection=np.sign(endX-startX)
    yDirection=np.sign(endY-startY)

    for inc in range(lineLength+1):
        map[startX+(inc*xDirection)][startY+(inc*yDirection)]+=1
    return map


linesList=[]
with open('05_input.txt') as f:
    allLines = f.readlines()
    for line in allLines:
        linesList.append([int(i) for i in line.strip().replace(' -> ',',').split(',')])

lines=np.array(linesList)

sizeX=max(max(lines[:,0]),max(lines[:,2]))+1
sizeY=max(max(lines[:,1]),max(lines[:,3]))+1

#part 1
map=np.zeros((sizeX, sizeY))
for line in linesList:
    if (line[0]==line[2]) | (line[1]==line[3]):   #only consider vertical or horizontal liones
        addHorizontalAndVerticalLines(line[0],line[1],line[2],line[3],map)
#print(np.transpose(map)) #transposed to match example format

numDangerPoints=(map>1).sum()
print("Part 1 answer:",numDangerPoints)


#part 2
for line in linesList:
    if not(line[0]==line[2]) | (line[1]==line[3]):   #only consider diagonal liones
        addDiagonalLines(line[0],line[1],line[2],line[3],map)
#print(np.transpose(map)) #transposed to match example format

numDangerPoints=(map>1).sum()
print("Part 2 answer:",numDangerPoints)
