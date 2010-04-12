#!/usr/bin/python
#debugging.py

class Debug:

    def __init__(self):
        pass

    @staticmethod
    def printTransmitInfo(Info):
        print "Tx: %s" % Info

    @staticmethod
    def printReceiveInfo(Info):
        print "Rx: %s" % Info

    @staticmethod
    def printStatusByte(ByteOne,ByteTwo):
        print "SW1:%02x,SW2:%02x" % (ByteOne,ByteTwo)
