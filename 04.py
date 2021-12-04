#!/usr/bin/python3
import numpy as np

boards=[]
dabs=[]
boardSize=5

def checkForWin(dabs):
    win=False
    needed=[True,True,True,True,True]
    for row in range(boardSize):
        #print(dabs)
        win = win | np.array_equal(dabs[:,row],needed) | np.array_equal(dabs[row],needed)
        if win:
            break
    return win

def score(board,dabs,calledNum):
    return int((board*(dabs==False)).sum()*calledNum)

with open('04_input.txt') as f:
    lines = f.readlines()
    numbersToBeCalled=[int(i) for i in lines[0].strip().split(',')]

    boardIndex=-1
    for line in lines[1:]:
        if line.strip()=='':
            boardIndex+=1
            rowIndex=0
            boards.append(np.zeros((boardSize, boardSize)))
            dabs.append(np.zeros((boardSize, boardSize))!=0)
        else:
            boards[boardIndex][rowIndex]=[int(i) for i in line.strip().split()]
            rowIndex+=1

    numBoards=boardIndex+1

#print(numBoards)
#print(numbersToBeCalled)
#print(boards)
#print(dabs)

#part 1
won=False
winningScore=0
for calledNum in numbersToBeCalled:
    for boardIndex in range(numBoards):
        dabs[boardIndex]=np.logical_or(dabs[boardIndex],boards[boardIndex]==calledNum)
        won=checkForWin(dabs[boardIndex])
        if won:
            #print(boards[boardIndex])
            winningScore=score(boards[boardIndex],dabs[boardIndex],calledNum)
            break
    if won:
        break

print("Part 1 answer:",winningScore)


#part 2
won=False
boardsWon=np.zeros(numBoards)!=0
winningScore=0
for calledNum in numbersToBeCalled:
    for boardIndex in range(numBoards):
        if boardsWon[boardIndex]==False:
            dabs[boardIndex]=np.logical_or(dabs[boardIndex],boards[boardIndex]==calledNum)
            boardsWon[boardIndex]=checkForWin(dabs[boardIndex])

            if boardsWon[boardIndex]:
                winningScore=score(boards[boardIndex],dabs[boardIndex],calledNum)


print("Part 2 answer:",winningScore)
