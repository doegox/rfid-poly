#!/usr/bin/python
#dataHandler.py
import string

def findNumberInString(cmd):
    return int(cmd[4])

def stringToArray(cmd):
    apdu = []
    index = 0
    while index < len(cmd):
        apdu.append(int(cmd[index:index+2],16))
        index += 3
    return apdu
        
