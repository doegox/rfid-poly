from smartcard.System import *
from smartcard.util import *
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

    def disconnect(self,connection):
        connection.disconnect()
        
