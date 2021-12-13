#!/usr/bin/python3
import numpy as np

with open('13_input.txt') as f:
    lines = f.readlines()

numCols=0
numRows=0
dots=[]
foldDetails=[]
for line in lines:
    if line.startswith('fold'):
        foldDetails.append(line.strip().split()[2].split('='))
        continue
    if line.strip()=='':
        continue
    coords=line.strip().split(',')
    xPos=int(coords[0])
    yPos=int(coords[1])
    dots.append((xPos,yPos))
    if xPos+1>numCols:
        numCols=xPos+1
    if yPos+1>numRows:
        numRows=yPos+1

sheet=np.zeros((numCols,numRows))
for dot in dots:
    sheet[dot]=1

sheet=np.transpose(sheet)

def doFolding(sheet,foldDetails):
    for fold in foldDetails:
        foldPoint=int(fold[1])
        if fold[0]=='y':
            topPart=sheet[:foldPoint,:]
            bottomPart=sheet[foldPoint+1:,:]
            bottomPart=bottomPart[::-1,:]
            numBottomRows=len(bottomPart)
            numTopRows=len(topPart)

            offset=abs(numTopRows-numBottomRows)
            if numBottomRows>=numTopRows:
                sheet=bottomPart
                for index in range(numTopRows):
                    sheet[index+offset,:]+=topPart[index,:]
            else:
                sheet=topPart
                for index in range(numBottomRows):
                    sheet[index+offset,:]+=bottomPart[index,:]
        else:
            leftPart=sheet[:,:foldPoint]
            rightPart=sheet[:,foldPoint+1:]
            rightPart=rightPart[:,::-1]
            numleftCols=len(leftPart[0])
            numRightCols=len(rightPart[0])

            numRows=len(leftPart)
            offset=abs(numleftCols-numRightCols)
            if numleftCols>=numRightCols:
                sheet=leftPart
                for row in range(numRows):
                    sheet[row,offset:]+=rightPart[row,:]
            else:
                sheet=rightPart
                for row in range(numRows):
                    sheet[row,offset:]+=leftPart[row,:]
        sheet[sheet>1]=1
    return sheet

#part 1
foldedSheet=doFolding(sheet,[foldDetails[0]])
print("Part 1 answer:",sum(sum(foldedSheet)))


#part 2
foldedSheet=doFolding(sheet,foldDetails)
print("Part 2 answer:")
for row in range(len(foldedSheet)):
    for col in range(len(foldedSheet[0])):
        if int(foldedSheet[row,col]):
            print("#",end='')
        else:
            print(" ",end='')
    print("")
