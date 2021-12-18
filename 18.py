#!/usr/bin/python3
import ast

with open('18_input.txt') as f:
    lines = f.readlines()

def parseInput(lines):
    numberList = []
    for line in lines:
        numberList.append(ast.literal_eval(line.strip()))
    return numberList

def magnitude(num):
    if isinstance(num, list):
        return 3*magnitude(num[0])+2*magnitude(num[1])
    else:
        return num

def add(num1,num2):
    return reduce([num1,num2])

def reduce(num):
    explodedNum=explode(num)
    if explodedNum!=num:  # exploded so there may be more to explode
        return reduce(explodedNum)
    else: # no explodes so let's try splitting
        newNum=splitNum(num)
        if newNum!=num:  # our splitting may have created nodes to explode again
            return reduce(newNum)
        else:
            return num

def explode(num):
    numStr=str(num)
    indexOfLastSeenNum=-1
    openBracketCount=0
    for ind in range(len(numStr)):
        openBracketCount+=numStr[ind]=='['
        openBracketCount-=numStr[ind]==']'
        if openBracketCount>4:
            pairEndIndex=ind
            while numStr[pairEndIndex]!=']':
                pairEndIndex+=1
            strBefore=numStr[:ind]
            strAfter=numStr[pairEndIndex+1:]
            pair=ast.literal_eval(numStr[ind:pairEndIndex+1])
            firstNum=pair[0]
            secondNum=pair[1]
            # track back to add to previous num
            for bwdInd in range(len(strBefore)-2,0,-1):
                if strBefore[bwdInd].isnumeric():
                    searchInd=bwdInd
                    while strBefore[searchInd].isnumeric():
                        searchInd-=1
                    numOfInterest=int(strBefore[searchInd+1:bwdInd+1])+firstNum
                    strBefore=strBefore[:searchInd+1]+str(numOfInterest)+strBefore[bwdInd+1:]
                    break

            # track forward to add to next num
            for fwdInd in range(len(strAfter)):
                if strAfter[fwdInd].isnumeric():
                    searchInd=fwdInd
                    while strAfter[searchInd].isnumeric():
                        searchInd+=1
                    numOfInterest=int(strAfter[fwdInd:searchInd])+secondNum
                    strAfter=strAfter[:fwdInd]+str(numOfInterest)+strAfter[searchInd:]
                    break

            return ast.literal_eval(strBefore+'0'+strAfter)
    return num

def splitNum(num):
    if isinstance(num, list):
        newNum=splitNum(num[0])
        if newNum!=num[0]:
            return [newNum,num[1]]
        else:
            newNum=splitNum(num[1])
            return [num[0],newNum]
    else:
        if num>9:
            return [num//2, (num+1)//2]
        else:
            return num


numberList=parseInput(lines)

#part 1
finalNumber=numberList[0]
for numIndex in range(1,len(numberList)):
    finalNumber=add(finalNumber,numberList[numIndex])
print("Part 1 answer:",magnitude(finalNumber))

#part 2
biggestMagnitude=0
for firstNum in numberList:
    for secondNum in numberList:
        if firstNum!=secondNum:
            mag=magnitude(add(firstNum,secondNum))
            if mag>biggestMagnitude:
                biggestMagnitude=mag

print("Part 2 answer:",biggestMagnitude)
