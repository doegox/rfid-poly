#!usr/bin/python
#pcsc_reader.py

from smartcard.System import *
from smartcard.util import *
from smartcard.CardRequest import CardRequest
from smartcard.CardType import AnyCardType
import reader


class PCSC_Reader(reader.abstractReader):

    def __init__(self):
        reader.abstractReader.__init__(self)

    def isTagConnected(self):
        raise NotImplementedError,"Cannot call abstract method"

    def isTagReleased(self):
        raise NotImplementedError,"Cannot call abstract method"

    def getReaderInfo(self):
        raise NotImplementedError,"Cannot call abstract method"

    def getConnectedTag(self):
        raise NotImplementedError,"Cannot call abstract method"


    def getConnectionToTag(self,reader):
        return reader.createConnection()

    def connect(self,connection):
        try:
            connection.connect()
            return True
        except:
            return False
        
    def doTransmition(self,connection,commandSet):
        try:
            return connection.transmit(commandSet)
        except:
            print "Transmitting error."

    #universal polling function(can be overwritten for specified kind of readers.(eg.TouchaTag)
    def pollForATag(self):
        cardtype = AnyCardType()
        cardrequest = CardRequest(timeout = 0.01,cardType=cardtype)
        try:
            cardservice = cardrequest.waitforcard()
            return True
        except:
            return False

    def disconnect(self,connection):
        connection.disconnect()

    #when the reader is removed, kill the reader instance    
    def kill(self):
        raise NotImplementedError,"Cannot call abstract method"
