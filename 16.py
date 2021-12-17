#!/usr/bin/python3
import numpy as np

hexToBin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

with open('16_input.txt') as f:
    lines = f.readlines()
binSeq=''.join(hexToBin.get(ch, ch) for ch in lines[0].strip())


def processPacket(packet):
    global versionRunningSum
    packetVersion=int(packet[0:3],2)
    versionRunningSum+=packetVersion
    packetTypeID=int(packet[3:6],2)
    packetLength=6
    if packetTypeID==4:  # literal value
        lastChunk=packet[6]=='0'
        payload=packet[7:11]
        offset=5
        packetLength+=offset
        chunkCount=1
        while not lastChunk:
            payload+=packet[7+(offset*chunkCount):11+(offset*chunkCount)]
            lastChunk=packet[6+(offset*chunkCount)]=='0'
            chunkCount+=1
            packetLength+=offset
        return int(payload, 2),packet[packetLength:]
    else:  # operator
        payloads=[]
        lengthTypeID=int(packet[6], 2)
        remainingPacket=''
        if lengthTypeID==0:  # next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
            subPacketLength=int(packet[7:22], 2)
            remainingPacket=packet[22:22+subPacketLength]
            while len(remainingPacket)>0:
                pl,remainingPacket=processPacket(remainingPacket)
                payloads.append(pl)
            remainingPacket=packet[(22+subPacketLength):]
        else:  # next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
            numSubpackets=int(packet[7:18], 2)
            remainingPacket=packet[18:]
            for subpacket in range(numSubpackets):
                pl,remainingPacket=processPacket(remainingPacket)
                payloads.append(pl)
        if packetTypeID==0:
            value=sum(payloads)
        elif packetTypeID==1:
            value=np.prod(payloads)
        if packetTypeID==2:
            value=min(payloads)
        if packetTypeID==3:
            value=max(payloads)
        if packetTypeID==5:
            value=int(payloads[0]>payloads[1])
        if packetTypeID==6:
            value=int(payloads[0]<payloads[1])
        if packetTypeID==7:
            value=int(payloads[0]==payloads[1])
        return value,remainingPacket




#part 1
versionRunningSum=0
a,b=processPacket(binSeq)
print("Part 1 answer:",versionRunningSum)

#part 2
value,b=processPacket(binSeq)
print("Part 2 answer:",value)
