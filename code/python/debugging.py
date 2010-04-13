#!/usr/bin/python
#debugging.py

try:
   from WConio import *
except:
   pass

class Debug:

    def __init__(self):
        pass

    @staticmethod
    def printTransmitInfo(Info):
        try:
            textcolor(LIGHTRED)
        except:
            pass
        print "Tx: %s" % Info
        try:
            textcolor(BLACK)
        except:
            pass

    @staticmethod
    def printReceiveInfo(Info):
        try:
            textcolor(LIGHTRED)
        except:
            pass
        print "Rx: %s" % Info
        try:
            textcolor(BLACK)
        except:
            pass

    @staticmethod
    def printStatusByte(ByteOne,ByteTwo):
        try:
            textcolor(LIGHTRED)
        except:
            pass
        print "SW1:%02x,SW2:%02x" % (ByteOne,ByteTwo)
        try:
            textcolor(BLACK)
        except:
            pass

    @staticmethod
    def printReadableInfo(obj,eventInfo):
        try:
            textcolor(LIGHTRED)
        except:
            pass
        print "%s%s" % (obj,eventInfo)
        try:
            textcolor(BLACK)
        except:
            pass
