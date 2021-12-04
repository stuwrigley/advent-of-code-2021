#!/usr/bin/python3
import numpy

report=[]

with open('03_input.txt') as f:
    lines = f.readlines()
    for line in lines:
        report.append(line.strip())

numRows=len(report)
numBits=len(report[0])

#part 1
gamma=0
epsilon=0
gamma_code=['0']*numBits
epsilon_code=['0']*numBits

true_count=numpy.zeros(numBits)
for bit_index in range(numBits):
    for row in report:
        true_count[bit_index]+=int(row[bit_index])
    if true_count[bit_index]>(numRows/2):
        gamma_code[bit_index]='1'
    else:
        epsilon_code[bit_index]='1'

gamma=int("".join(gamma_code),2)
epsilon=int("".join(epsilon_code),2)

print("Part 1 answer:",gamma*epsilon)


#part 2
oxygen_code=report.copy()
co2_code=report.copy()
for bit_index in range(numBits):

    if len(oxygen_code)>1:
        oxygenCountOfOnes=0
        tempOxygen=[]
        for row in oxygen_code:
            oxygenCountOfOnes+=int(row[bit_index])
        mostCommonBit=int(oxygenCountOfOnes>=(len(oxygen_code)/2))

        for row in oxygen_code:
            if int(row[bit_index])==mostCommonBit:
                tempOxygen.append(row)
        oxygen_code=tempOxygen


    if len(co2_code)>1:
        co2CountOfOnes=0
        tempCo2=[]
        for row in co2_code:
            co2CountOfOnes+=int(row[bit_index])
        leastCommonBit=int(co2CountOfOnes<(len(co2_code)/2))

        for row in co2_code:
            if int(row[bit_index])==leastCommonBit:
                tempCo2.append(row)
        co2_code=tempCo2

oxygen=int("".join(oxygen_code),2)
co2=int("".join(co2_code),2)

print("Part 2 answer:",oxygen*co2)
