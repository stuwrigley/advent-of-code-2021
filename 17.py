#!/usr/bin/python3

input='target area: x=217..240, y=-126..-69'
minX=217
maxX=240
minY=-126
maxY=-69

def onTarget(loc):
    return (minX <= loc[0] <= maxX) and (minY <= loc[1] <= maxY)

def fireProbe(xVel, yVel):
    heighestPoint=0
    passedTargetArea=False
    x=0; y=0
    while not passedTargetArea:
        x+=xVel
        y+=yVel
        if y>heighestPoint:
            heighestPoint=y
        if onTarget(((x,y))):
            return True,heighestPoint
        if xVel!=0:
            if xVel>0:
                xVel+=-1
            else:
                xVel+=1
        yVel+=-1
        passedTargetArea=x>maxX or y<minY
    return False,heighestPoint

#part 1
heighestPoint=0
count=0
for xVel in range(maxX+1):
    for yVel in range(-200,200):
        hit,height=fireProbe(xVel, yVel)
        if hit and height>heighestPoint:
            heighestPoint=height
        count+=hit
print("Part 1 answer:",heighestPoint)

#part 2
print("Part 2 answer:",count)
