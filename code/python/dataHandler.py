#!/usr/bin/python
#dataHandler.py
import string
from database import *
from debugging import Debug

def findNumberInString(cmd):
    return int(cmd[4])

def stringToArray(cmd):
    try:
       apdu = []
       index = 0
       while index < len(cmd):
             apdu.append(int(cmd[index:index+2],16))
             index += 3
       return apdu
    except ValueError:
       #incorrect format of apdu may cause this type of exception
       return None
    except:
       assert(False)

def findTagsNotInEnum(tagList):
    NotInEnum = []
    for tagtype in tagTypes:
        if tagtype != UNKNOWN and not tagtype in tagList:
            NotInEnum.append(tagtype)
    return NotInEnum
