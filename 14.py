#!/usr/bin/python3
import numpy as np
import collections

with open('14_input.txt') as f:
    lines = f.readlines()

template=lines[0].strip()
rules=dict()
for line in lines[2:]:
    parts=line.strip().split(' -> ')
    rules[parts[0]]=parts[1]

def doExpansion(template,numExpansions):
    polymer=template
    for step in range(numExpansions):
        newPolymer=''
        for i in range(len(polymer)-1):
            newPolymer+=polymer[i]+rules[polymer[i:i+2]]#+polymer[i+1]
        newPolymer+=polymer[-1]
        polymer=newPolymer
    return polymer

def doExpansionByCounts(template,numExpansions):
    template+='$'
    polymer=dict()
    for i in range(len(template)-1):
        section=template[i:i+2]
        if section not in list(polymer):
            polymer[section]=0
        polymer[section]+=1

    for step in range(numExpansions):
        oldPolymer=polymer
        polymer=dict()
        for pair in list(oldPolymer):
            if pair[1]!='$':
                newPair1=pair[0]+rules[pair]
                newPair2=rules[pair]+pair[1]
                if newPair1 not in list(polymer):
                    polymer[newPair1]=0
                if newPair2 not in list(polymer):
                    polymer[newPair2]=0
                polymer[newPair1]+=oldPolymer[pair]
                polymer[newPair2]+=oldPolymer[pair]
            else:
                polymer[pair]=oldPolymer[pair]
    return polymer

#part 1
polymer=doExpansion(template,10)
counts=collections.Counter(polymer).most_common()
print("Part 1 answer:",counts[0][1]-counts[-1][1])


#part 2... can't do it the same way as part 1... have to be cleverer!

def getScoreFromPolymerDict(polymer):
    letterCounts=dict()
    for pair in list(polymer):
        if pair[0] not in list(letterCounts):
            letterCounts[pair[0]]=0
        letterCounts[pair[0]]+=polymer[pair]
    return max(letterCounts.values())-min(letterCounts.values())

polymer=doExpansionByCounts(template,40)
score=getScoreFromPolymerDict(polymer)
print("Part 2 answer:",score)
