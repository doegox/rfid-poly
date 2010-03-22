#!usr/bin/python
#ACS_ACU122.py

import pcsc_reader
from readerInfo import readerInfo
#libraries for testing reason
from smartcard.System import *
from smartcard.util import *
import time

class ACS_ACU122(pcsc_reader.PCSC_Reader):

      def __init__(self,reader):
          pcsc_reader.PCSC_Reader.__init__(self)
          self.readerInfo = readerInfo(reader.name,self.readername,self.hardware,self.supportProtocols,self.supportTagTypes)
          self.connection = self.getConnectionToTag(reader)
          self.connect(self.connection)
          #set retry time to 1
          self.doTransmition(self.connection,self.commandSet['setRetryTime'])


      #parameters of touchatag    
      readername = 'ACS ACR 38U'
      hardware = 'PN532'
      supportProtocols = ('ISO14443A/B','ISO18092')
      supportTagTypes = ('Mifare Ultralight','Mifare 1K','Mifare 4K')

      #command sets
      commandSet = {'setRetryTime':[0xFF,0x00,0x00,0x00,0x06,0xD4,0x32,0x05,0x00,0x00,0x00],
                    'pollingCommand':[0xFF,0x00,0x00,0x00,0x04,0xD4,0x4A,0x01,0x00],
                    'getResponse':[0xFF,0xC0,0x00,0x00]}

      #runtime variable
      tagType = None
      tagUID = None
      tagConnect = False
      tagRelease = False
      releaseCheckRunning = False
      connectCheckRunning = False
      
      def isTagConnected(self):
            if not self.releaseCheckRunning:
                self.connectCheckRunning = True
                self.__pollForATag()
                self.connectCheckRunning = False
            return self.tagConnect

      def isTagReleased(self):
            if not self.connectCheckRunning:
                self.releaseCheckRunning = True
                self.__pollForATag()
                self.connectCheckRunning = False
            return self.tagRelease

      def __pollForATag(self):
             data,trans1,trans2 = self.doTransmition(self.connection,self.commandSet['pollingCommand'])
             self.commandSet['getResponse'].append(trans2)
             result,get1,get2 = self.doTransmition(self.connection,self.commandSet['getResponse'])
             self.commandSet['getResponse'].pop()
             #operate the runtime variables according to the reponse of the direct transmit and get response data
             if hex(trans2) == '0x5':
                 self.tagConnect = False
                 if self.tagType == None:
                     self.tagRelease = False
                 else:
                     self.tagRelease = True
                     self.tagType = None
                     self.tagUID = None
             elif hex(trans2) == '0xe':
                 self.tagRelease = False
                 if self.tagType == None:
                     self.tagConnect = True
                     self.tagUID = result[8:12]
                     self.tagType = result[6]
                 else:
                     self.tagConnect = False
                #fake polling
                 data,trans1,trans2 = self.doTransmition(self.connection,self.commandSet['pollingCommand'])
             elif hex(trans2) == '0x11':
                 self.tagRelease = False
                 if self.tagType == None:
                     self.tagConnect = True
                     self.tagUID = result[8:15]
                     self.tagType = result[6]
                 else:
                     self.tagConnect = False
                #fake polling
                 data,trans1,trans2 = self.doTransmition(self.connection,self.commandSet['pollingCommand'])
             else:
                 pass
                 
             
      def getConnectedTag(self):
          pass

          
      def getReaderInfo(self):
          return self.readerInfo
      

#self-testing
if __name__ == '__main__':
        acs = ACS_ACU122(readers()[0])
        while True:
                  if acs.isTagConnected():
                      print toHexString(acs.tagUID)+" connected!"
                  if acs.isTagReleased():
                      print "tag released!"
                                         
