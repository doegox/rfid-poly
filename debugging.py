#!/usr/bin/python
#debugging.py

from smartcard.util import *
import os

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
        if os.name == 'posix':
           print '\033[31m'
        print "Tx: %s" % Info
        if os.name == 'posix':
           print '\033[30m'
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
        if os.name == 'posix':
           print '\033[31m'
        print "Rx: %s" % Info
        if os.name == 'posix':
           print '\033[30m'
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
        if os.name == 'posix':
           print '\033[31m'
        print "SW1:%02x,SW2:%02x" % (ByteOne,ByteTwo)
        if os.name == 'posix':
           print '\033[30m'
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
        if os.name == 'posix':
           print '\033[31m'
        print "%s%s" % (obj,eventInfo)
        if os.name == 'posix':
           print '\033[30m'
        try:
            textcolor(BLACK)
        except:
            pass
    @staticmethod
    def APDUDecoding(apdu):
        try:
            textcolor(LIGHTRED)
        except:
            pass
        if os.name == 'posix':
           print '\033[31m'
        print "The APDU you entered is: %s" % toHexString(apdu)
        if len(apdu) < 4:
           print "The APDU is illegal and it may cause exceptions." 
        else:
           print 'CLA'.ljust(5,' '),'INS'.ljust(5,' '),'P1'.ljust(5,' '),'P2'.ljust(5,' '),'EXTENTED_BYTES'.ljust(20,' ')
           for i in range(4):
               print '%02x'.ljust(7,' ') % apdu[i],
           try:
               print toHexString(apdu[4:]).ljust(20,' ')
           except:
               print 'EMPTY'.ljust(20,' ')
        if os.name == 'posix':
           print '\033[30m'
        try:
            textcolor(BLACK)
        except:
            pass
