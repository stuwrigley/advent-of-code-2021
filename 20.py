#!/usr/bin/python3

with open('20_input.txt') as f:
    lines = f.readlines()

def parseInput(lines):
    lookup=lines[0].strip()
    image=[]
    for line in lines[2:]:
        image.append(line.strip())
    return lookup,image

def enhance(image,lookup,numPasses=1):
    for enhancementPass in range(numPasses):
        newImage=[]
        for rowInd in range(len(image)):
            newRow=''
            for colInd in range(len(image[0])):
                pointerStr=''
                for rowShift in range(rowInd-1,rowInd+2,1):
                    for colShift in range(colInd-1,colInd+2,1):
                        if 0<=rowShift<len(image) and 0<=colShift<len(image[0]):
                            pointerStr+=image[rowShift][colShift]
                        else:
                            pointerStr+='.'
                pointerStr=pointerStr.replace('.','0')
                pointerStr=pointerStr.replace('#','1')
                ptr=int(pointerStr,2)
                newRow+=lookup[ptr]
            newImage.append(newRow)
        image=newImage
    return newImage


def padImage(img,paddingSize):
    newImg=[]
    for pad in range(paddingSize):
        newImg.append("." * (len(img[0])+paddingSize*2))
    padding="." * paddingSize
    for row in img:
        newImg.append(padding+row+padding)
    for pad in range(paddingSize):
        newImg.append("." * (len(img[0])+paddingSize*2))
    return newImg

def clipImage(image,paddingSize):
    clippedImage=[]
    for rowInd in range(paddingSize,len(image)-paddingSize+1):
        clippedImage.append(image[rowInd][paddingSize:len(image)-paddingSize])
    return clippedImage


def printImage(img):
    for row in range(len(img)):
        print(img[row])

def countHashes(img):
    count=0
    for row in img:
        count+=row.count('#')
    return count


lookup,image=parseInput(lines)

#part 1
numIterations=2
paddingSize=100  # dirty way to cope with the infinite size
paddedImage=padImage(image,paddingSize)
newImage=enhance(paddedImage,lookup,numIterations)
clippedImage=clipImage(newImage,numIterations)
print("Part 1 answer:",countHashes(clippedImage))

#part 2
numIterations=50
paddingSize=100  # dirty way to cope with the infinite size
paddedImage=padImage(image,paddingSize)
newImage=enhance(paddedImage,lookup,numIterations)
clippedImage=clipImage(newImage,numIterations)
print("Part 2 answer:",countHashes(clippedImage))
