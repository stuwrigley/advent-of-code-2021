#!/usr/bin/python3
import numpy as np

numRolesPerPlayer=3
highestSide=100
highestPosition=10
maxScore=1000   # part 1

playerPosition=[6,9]  # actual data
playerScores=np.array([0,0])

#playerPosition=[4,8]  # test data


def rollDie(nextFace,numRoles):
    nextFace=((nextFace-1)%highestSide)+1
    thisSum=0
    for roll in range(numRolesPerPlayer):
        nextFace=((nextFace-1)%highestSide)+1
        thisSum+=nextFace
        nextFace+=1
    return thisSum,nextFace

#part 1
nextFace=1
dieRollCount=0
while True:
    for player in range(len(playerPosition)):
        thisSum,nextFace=rollDie(nextFace,numRolesPerPlayer)
        newPosition=playerPosition[player]+thisSum
        playerPosition[player]=((newPosition-1)%highestPosition)+1
        playerScores[player]+=playerPosition[player]
        dieRollCount+=numRolesPerPlayer
        #print("Player",player+1,"roles",thisSum,"to move to space",playerPosition[player],"for a total score of",playerScores[player])
        if any(playerScores>=maxScore):
            break
    if any(playerScores>=maxScore):
        break


score=min(playerScores)*dieRollCount
print("Part 1 answer:",score)

#part 2
print("Part 2 answer:")
