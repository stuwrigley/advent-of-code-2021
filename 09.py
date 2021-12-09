#!/usr/bin/python3
import numpy as np
import math

with open('09_input.txt') as f:
    lines = f.readlines()

numRows=len(lines)
numCols=len(lines[0].strip())

heightmap=np.zeros((numRows,numCols))
for rowNum in range(numRows):
    heightmap[rowNum]=(np.array([int(i) for i in lines[rowNum].strip()]))

def findLocalMinima(heightmap):
    minimamap=np.zeros((numRows,numCols))
    for rowNum in range(numRows):
        for colNum in range(numCols):
            currentHeight=heightmap[rowNum][colNum]
            adjacents=[]
            if colNum>0:
                adjacents.append(heightmap[rowNum][colNum-1])
            if colNum<(numCols-1):
                adjacents.append(heightmap[rowNum][colNum+1])
            if rowNum>0:
                adjacents.append(heightmap[rowNum-1][colNum])
            if rowNum<(numRows-1):
                adjacents.append(heightmap[rowNum+1][colNum])
            adjacents=np.array(adjacents)
            if all(currentHeight<adjacents):
                minimamap[rowNum][colNum]=1
    return minimamap

#part 1
minimaMap=findLocalMinima(heightmap)
maskedHeightMap=np.ma.masked_where(minimaMap==0, heightmap)
minimaHeights=np.ma.compressed(maskedHeightMap)
score=sum(minimaHeights+1)
print("Part 1 answer:",score)


#part 2
def considerPoint(heightmap,position,explored):
    explored.add(position)
    row,col=position
    currentHeight=heightmap[position]
    if col>0:
        nextPos=(row,col-1)
        explored=processNextPoint(heightmap,currentHeight,nextPos,explored)
    if col<(numCols-1):
        nextPos=(row,col+1)
        explored=processNextPoint(heightmap,currentHeight,nextPos,explored)
    if row>0:
        nextPos=(row-1,col)
        explored=processNextPoint(heightmap,currentHeight,nextPos,explored)
    if row<(numRows-1):
        nextPos=(row+1,col)
        explored=processNextPoint(heightmap,currentHeight,nextPos,explored)
    return explored

def processNextPoint(heightmap,currentHeight,nextPos,explored):
    nextHeight=heightmap[nextPos]
    if nextPos not in explored and nextHeight>currentHeight and nextHeight<9:
        nextNeighbourhood=considerPoint(heightmap,nextPos,explored)
        explored=explored.union(nextNeighbourhood)
    return explored


numBasins=len(minimaHeights)
minimaLocations=np.where(minimaMap)
basinSizes=[]
for basinID in range(numBasins):
    curPos=((minimaLocations[0][basinID],minimaLocations[1][basinID]))
    basinSizes.append(len(considerPoint(heightmap,curPos,set())))

score=np.prod(sorted(basinSizes)[-3:])
print("Part 2 answer:",score)
