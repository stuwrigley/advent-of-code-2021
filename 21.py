#!/usr/bin/python3
from collections import defaultdict
import numpy as np

numRolesPerPlayer=3
highestPosition=10
playerScore=np.array([0,0])


def rollDie(nextFace,numRoles):
    nextFace=((nextFace-1)%highestSide)+1
    thisSum=0
    for roll in range(numRolesPerPlayer):
        nextFace=((nextFace-1)%highestSide)+1
        thisSum+=nextFace
        nextFace+=1
    return thisSum,nextFace



#part 1
playerPosition=[6,9]  # actual data
#playerPosition=[4,8]  # test data
maxScore=1000
highestSide=100
nextFace=1
dieRollCount=0
while True:
    for player in range(len(playerPosition)):
        thisSum,nextFace=rollDie(nextFace,numRolesPerPlayer)
        newPosition=playerPosition[player]+thisSum
        playerPosition[player]=((newPosition-1)%highestPosition)+1
        playerScore[player]+=playerPosition[player]
        dieRollCount+=numRolesPerPlayer
        #print("Player",player+1,"roles",thisSum,"to move to space",playerPosition[player],"for a total score of",playerScores[player])
        if any(playerScore>=maxScore):
            break
    if any(playerScore>=maxScore):
        break

score=min(playerScore)*dieRollCount
print("Part 1 answer:",score)



#part 2
playerPosition=(6,9)  # actual data
#playerPosition=(4,8)  # test data
maxScore=21
highestSide=3
playerScore=(0,0)
playerWinCount=[0,0]

def completeGame(playerPosition,playerScore,currentPlayer):
    for roll1 in range(1,highestSide+1):
        for roll2 in range(1,highestSide+1):
            for roll3 in range(1,highestSide+1):
                newPosition=[*playerPosition]
                newScore=[*playerScore]
                newPosition[currentPlayer]=playerPosition[currentPlayer]+roll1+roll2+roll3
                newPosition[currentPlayer]=((newPosition[currentPlayer]-1)%highestPosition)+1
                newScore[currentPlayer]+=newPosition[currentPlayer]
                if newScore[currentPlayer]>=maxScore:
                    playerWinCount[currentPlayer]+=1
                    print("\rWins:",playerWinCount,end='')
                    return
                currentPlayer=(currentPlayer+1)%2
                completeGame(newPosition,newScore,currentPlayer)

#completeGame(list(playerPosition),list(playerScore),0)  # computing every possible universe will take too long...

gameStates=defaultdict(int)
gameStates[playerPosition,playerScore,0]=1
while gameStates:
    playerPosition,playerScore,currentPlayer=min(gameStates.keys(), key=lambda score:score[1][0]+score[1][1])
    stateCount = gameStates.pop((playerPosition,playerScore,currentPlayer))
    for roll1 in range(1,highestSide+1):
        for roll2 in range(1,highestSide+1):
            for roll3 in range(1,highestSide+1):
                newPosition=list(playerPosition)
                newScore=list(playerScore)
                newPosition[currentPlayer]=playerPosition[currentPlayer]+roll1+roll2+roll3
                newPosition[currentPlayer]=((newPosition[currentPlayer]-1)%highestPosition)+1
                newScore[currentPlayer]=playerScore[currentPlayer]+newPosition[currentPlayer]
                if newScore[currentPlayer]>=maxScore:
                    playerWinCount[currentPlayer]+=stateCount
                else:
                    nextPlayer=(currentPlayer+1)%2
                    gameStates[tuple(newPosition),tuple(newScore),nextPlayer]+=stateCount
                    #print("\rgameStates size:",len(gameStates),end='')

print("Part 2 answer:",max(playerWinCount))
