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
       apdu_str = [cmd]
       for separator in (' ',',',':'):
           if cmd.split(separator)[0] != cmd:
               apdu_str = cmd.split(separator)
               break
       for s in apdu_str:
           if len(s) > 2:
               return APDU_ERROR_TYPE_A
       for i in range(len(apdu_str)):
           apdu.append(int(apdu_str[i],16))
       return apdu
    except ValueError:
       #not all the bytes are in hexadecimal
       return APDU_ERROR_TYPE_B
    except:
       #---------------------------------------------------------------------------------------------------
       if DEBUG:
           Debug.printReadableInfo('ErrorFromDataHandlerStringToArrayMethod',': the algorithm is still not perfect.')
           Debug.printReadableInfo(cmd,': find problem when get this APDU.')
       #---------------------------------------------------------------------------------------------------
       assert(False)

def findTagsNotInEnum(tagList):
    NotInEnum = []
    for tagtype in tagTypes:
        if tagtype != UNKNOWN and not tagtype in tagList:
            NotInEnum.append(tagtype)
    return NotInEnum
