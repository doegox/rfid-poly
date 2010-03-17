import pcsc_reader
from readerInfo import readerInfo
#libraries for testing reason
from smartcard.System import *
from smartcard.util import *
import time

class OMNIKEY_Cardman5321(pcsc_reader.PCSC_Reader):

      def __init__(self,reader):
          pcsc_reader.PCSC_Reader.__init__(self)
          self.readerInfo = readerInfo(self.readername,self.hardware,self.supportProtocols,self.supportTagTypes)
          self.connection = self.getConnectionToTag(reader)

      #parameters of OMNIKEY Cardman 5321
      readername = "OMNIKEY CardMan 5x21-CL 0"
      hardware = "PN531"
      supportProtocols = ('ISO15693','ISO14443A/B')
      supportTagTypes = ('Mifare Ultralight','Mifare 1K','Mifare 4K','TagIT')

      #command sets
      hasAnOldTag = False

      
      
      def isTagConnected(self):
          if not self.hasAnOldTag:
             if self.connect(self.connection):
                 self.hasAnOldTag = True
             return self.hasAnOldTag
          else:
             return False

      def isTagReleased(self):
          if self.hasAnOldTag:
              if not self.connect(self.connection):
                  self.hasAnOldTag = False
              return not self.hasAnOldTag
          else:
              return False


      def getConnectedTag(self):
          pass

      def getReaderInfo(self):
          return self.readerInfo

#self-testing
if __name__ == '__main__':
    print "The program will exit if there is no tag action for 10secs"
    time0 = time.time()
    omi = OMNIKEY_Cardman5321(readers()[1])
    while time.time()-time0 < 10:
              if omi.isTagConnected():
                  print "new tag connected!"
                  time0 = time.time()
              if omi.isTagReleased():
                  print "tag released!"
                  time0 = time.time()
          
