#!/usr/bin/python3
import numpy as np
import math

patterns=[]
with open('08_input.txt') as f:
    lines = f.readlines()

#part 1
count=0
for line in lines:
    parts=line.split(' | ')
    output=parts[1].split()
    for digit in output:
        count+=(len(digit) in [2,4,3,7])
print("Part 1 answer:",count)

#part 2

def decodeInputs(inputs):
    sigPatternLengths=[len(sigPattern) for sigPattern in inputs]
    one = set(inputs[sigPatternLengths.index(2)])
    four = set(inputs[sigPatternLengths.index(4)])
    seven = set(inputs[sigPatternLengths.index(3)])
    eight = set(inputs[sigPatternLengths.index(7)])

    # display segments
    a=seven.difference(one)
    bd=four.difference(one)
    eg=eight.difference(four.union(seven))

    # horizontal segments common to 2, 3, and 5 (all have 5 segments lit)
    two_three_five = [inputs[i] for i,x in enumerate(sigPatternLengths) if x == 5]
    adg=set(two_three_five[0])
    for element in two_three_five[1:]:
        adg=adg.intersection(element)

    dg=adg.difference(a)
    d=dg.intersection(bd)
    b=bd.difference(d)
    g=dg.difference(d)
    e=eg.difference(g)

    nine=eight.difference(e)
    zero=eight.difference(d)

    # length 6 signal patterns are either 0 or 6 or 9
    zero_six_nine = [inputs[i] for i,x in enumerate(sigPatternLengths) if x == 6]
    six=set()
    for element in zero_six_nine:
        if set(element)!=nine and set(element)!=zero:
            six=set(element)

    c=eight.difference(six)
    f=one.difference(c)

    two=a.union(c).union(d).union(e).union(g)
    three=a.union(c).union(d).union(f).union(g)
    five=a.union(b).union(d).union(f).union(g)

    return {1:one, 2:two, 3:three, 4:four, 5:five, 6:six, 7:seven, 8:eight, 9:nine}



def decodeOutput(output,encoding):
    value=0
    for digitStrIndex in range(0,len(output)):
        for digit in range(1,len(encoding)+1):
            if set(output[digitStrIndex])==encoding[digit]:
                value+=digit*pow(10,3-digitStrIndex)
    return value

count=0
for line in lines:
    parts=line.split(' | ')
    encoding=decodeInputs(parts[0].split())
    count+=decodeOutput(parts[1].split(),encoding)

print("Part 2 answer:",count)
