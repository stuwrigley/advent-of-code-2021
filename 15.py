#!/usr/bin/python3
import numpy as np
import heapq

with open('15_input.txt') as f:
    lines = f.readlines()

riskMap=[list(map(int, line.strip())) for line in lines]
riskMap=np.array(riskMap)



def growMap(map,factor):
    numRows=len(riskMap)
    numCols=len(riskMap[0])
    bigRiskMap=np.zeros((numRows*factor,numCols*factor), dtype=int)
    for row in range(factor):
        for col in range(factor):
            bigRiskMap[(0+numRows*row):numRows*(row+1),(0+numCols*col):numCols*(col+1)]=riskMap+row+col
    bigRiskMap[bigRiskMap>9]-=9
    return bigRiskMap



def pathFinder(risk):
    paths=[(0, 0, 0)]
    visited=[[0] * len(row) for row in risk]
    while True:
        riskScore, x, y = heapq.heappop(paths)
        if not visited[x][y]:
            if x==len(risk)-1 and y==len(risk[x])-1:   # reached the end corner
                return riskScore
            visited[x][y]=1
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if (len(risk) > nx >= 0 <= ny < len(risk[0])) and not visited[nx][ny]:   # check new indices are in bounds and not visited
                    heapq.heappush(paths, (riskScore+risk[nx][ny], nx, ny))



#part 1
cost=pathFinder(riskMap)
print("Part 1 answer:",cost)

#part 2
bigRiskMap=growMap(riskMap,5)
cost=pathFinder(bigRiskMap)
print("Part 2 answer:",cost)
