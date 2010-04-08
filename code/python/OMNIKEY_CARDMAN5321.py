#!/usr/bin/python
#OMNIKEY_CARDMAN5321

import pcsc_reader
import string
from readerInfo import readerInfo
from database import *
from Mifare_Ultralight import Mifare_Ultralight
from Mifare_1K import Mifare_1K
from Mifare_4K import Mifare_4K
from UnknownTag import UnknownTag
#libraries for testing reason
from smartcard.System import *
from smartcard.util import *
import time

class OMNIKEY_Cardman5321(pcsc_reader.PCSC_Reader):

     def __init__(self,reader):
         pcsc_reader.PCSC_Reader.__init__(self,reader)
         self.reader = reader
         self.readerInfo = readerInfo(reader.name,self.readername,self.hardware,self.supportProtocols,self.supportTagTypes)
         self.connection = self.getConnectionToTag(reader)
         self.protocol = smartcard.scard.SCARD_PROTOCOL_T1

     #parameters of OMNIKEY Cardman 5321
     readername = OMNIKEY_CARDMAN_5321
     hardware = PN531
     supportProtocols = (ISO15693,ISO14443)
     supportTagTypes = (MIFARE_ULTRALIGHT,MIFARE_1K,MIFARE_4K,TAGIT)


     #commandSet
     commandSet = {'getUID':[0xFF,0xCA,0x00,0x00,0x00],
                   'readMifareUltralight':[0xFF,0xB0,0x00]
          }

     def getConnectedTag(self):
         self.connect(self.connection)
         atr = self.connection.getATR()
         tagUID,sw1,sw2 = self.doTransmition(self.connection,self.commandSet["getUID"],self.protocol)
         atr_len = len(atr) 
         if atr_len > 14:
              if hex(atr[14]) == NN[MIFARE_1K]:
                  return Mifare_1K(toHexString(tagUID),self.getATR(),self.reader.name)
              elif hex(atr[14]) == NN[MIFARE_4K]:
                  return Mifare_4K(toHexString(tagUID),self.getATR(),self.reader.name)
              elif hex(atr[14]) == NN[MIFARE_ULTRALIGHT]:
                  return Mifare_Ultralight(toHexString(tagUID),self.getATR(),self.reader.name)
              else:
                  print 'unsupported tag format(no Mifare 1k/4k/UL)'
                  return ( UnknownTag(toHexString(tagUID),self.getATR(),self.reader.name) )
         else:
              return ( UnknownTag(toHexString(tagUID),self.getATR(),self.reader.name) ) 

     def getReaderInfo(self):
         return self.readerInfo

     def transmitAPDU(self,apdu):
          self.connect(self.connection)
          return self.doTransmition(self.connection,apdu,self.protocol)

     def readMifareUltralight(self):
          self.connect(self.connection)
          tagData = []
          for i in range(16):
               self.commandSet['readMifareUltralight'].append(i)
               self.commandSet['readMifareUltralight'].append(16)
               data,sw1,sw2 = self.doTransmition(self.connection,self.commandSet['readMifareUltralight'],self.protocol)
               self.commandSet['readMifareUltralight'].pop()
               self.commandSet['readMifareUltralight'].pop()
               tagData.append(data[0:4])
          return tagData

     @staticmethod
     def isThisType(sysName,readerName):
          if sysName == 'posix':
               if readerName[-2:] == '01' and string.find(readerName,'OMNIKEY CardMan 5x21') == 0:
                  return True
               else:
                  return False
          elif sysName == 'nt':
               if string.find(readerName,'OMNIKEY CardMan 5x21-CL') == 0:
                  return True
               else:
                  return False
          else:
               raise NotImplementedError,"Sorry, this operating system is not supported by our software."

     def __del__(self):
         pass

#self-testing
if __name__ == '__main__':
   print "The program will exit if there is no tag action for 30secs"
   time0 = time.time()
   omi = OMNIKEY_Cardman5321(readers()[1])
   while time.time()-time0 < 30:
             omi.update()
             if omi.isTagConnected():
                   print "tag connect"
                   print omi.getConnectedTag().getTagInfo().getTagUID()
             if omi.isTagReleased():
                   print "tag remove"
