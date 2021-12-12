#!/usr/bin/python3
import numpy as np

with open('12_input.txt') as f:
    lines = f.readlines()

def createGraph(lines):
    graph=dict()
    for edge in lines:
        edgeNodes=edge.strip().split('-')
        if edgeNodes[0] not in graph:
            graph[edgeNodes[0]]=[]
        if edgeNodes[1] not in graph[edgeNodes[0]]:
            graph[edgeNodes[0]].append(edgeNodes[1])
        if edgeNodes[1] not in graph:
            graph[edgeNodes[1]]=[]
        if edgeNodes[0] not in graph[edgeNodes[1]]:
            graph[edgeNodes[1]].append(edgeNodes[0])
    return graph


def depthFirst(graph, currentVertex, visited, allTraversals, specialVertex):
    visited.append(currentVertex)
    allTraversals.append(visited)

    for vertex in graph[currentVertex]:
        forceVisit = (vertex==specialVertex and visited.count(specialVertex)<2)

        if vertex not in visited or forceVisit or vertex.isupper():   # allow upper case verices to be visited any number of times
            depthFirst(graph, vertex, visited.copy(), allTraversals, specialVertex)
    #allTraversals.append(visited)
    return allTraversals


graph=createGraph(lines)


def stripIncompleteTraversals(traversals):
    fullTraversals=[]
    for traversal in allTraversals:
        if traversal[-1]=='end':
            fullTraversals.append(traversal.copy())
    return fullTraversals


def printTraversals(traversals):
    for t in traversals:
        print(t)


#part 1
allTraversals=depthFirst(graph, 'start', [], [], '')  # but this includes partial traversals
fullTraversals=stripIncompleteTraversals(allTraversals)  # only keep 'complete' traversals - ie ones that end at "end"
print("Part 1 answer:",len(fullTraversals))


#part 2
smallCaves=[]
for cave in list(graph):
    if cave not in ['start','end'] and cave.islower():
        smallCaves.append(cave)

uniqueFullTraversals=[]
for smallCave in smallCaves:
    allTraversals=depthFirst(graph, 'start', [], [], smallCave)
    fullTraversals=stripIncompleteTraversals(allTraversals)  # only keep 'complete' traversals - ie ones that end at "end"
    for ft in fullTraversals:
        if ft not in uniqueFullTraversals:
            uniqueFullTraversals.append(ft)

print("Part 2 answer:",len(uniqueFullTraversals))
