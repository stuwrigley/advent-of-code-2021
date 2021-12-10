#!/usr/bin/python3
import numpy as np
import math

with open('10_input.txt') as f:
    lines = f.readlines()

openers=['(','[','{','<']
closers=[')',']','}','>']
matches={'(':')','[':']','{':'}','<':'>'}
scores={')':3,']':57,'}':1197,'>':25137}
competionScores={'(':1,'[':2,'{':3,'<':4}


def completeIncompleteLine(line):
    score=0
    stack=[]
    for char in list(line)[::-1]:
        if char in closers:
            stack.append(char)
        else:
            if len(stack)==0:
                score=score*5 + competionScores[char]
            else:
                stack.pop()
    return score

def isIncomplete(line):
    stack=[]
    for char in list(line):
        if char in openers:
            stack.append(char)
        if char in closers:
            if len(stack)>0:
                lastOpener=stack.pop()
                if char!=matches[lastOpener]:  # corrupt
                    return False
    return len(stack)>0



def processLine(line):
    stack=[]
    for char in list(line):
        if char in openers:
            stack.append(char)
        if char in closers:
            if len(stack)>0:  # ignore incomplete lines
                lastOpener=stack.pop()
                if char!=matches[lastOpener]:  # corrupt
                    return scores[char]
    return 0

#part 1
score=0
for line in lines:
    score+=processLine(line.strip())
print("Part 1 answer:",score)


#part 2
scores=[]
for line in lines:
    if isIncomplete(line):
        scores.append(int(completeIncompleteLine(line.strip())))
midIndex=int((len(scores)-1)/2)
score=sorted(scores)[midIndex]

print("Part 2 answer:",score)
