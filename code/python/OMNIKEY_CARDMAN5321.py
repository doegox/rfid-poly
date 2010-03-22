#!usr/bin/python
#OMNIKEY_CARDMAN5321

import pcsc_reader
import threading,thread
from readerInfo import readerInfo
#libraries for testing reason
from smartcard.System import *
from smartcard.util import *
import time

class OMNIKEY_Cardman5321(pcsc_reader.PCSC_Reader):

      def __init__(self,reader):
          pcsc_reader.PCSC_Reader.__init__(self)
          self.readerInfo = readerInfo(reader.name,self.readername,self.hardware,self.supportProtocols,self.supportTagTypes)
          self.connection = self.getConnectionToTag(reader)
          thread.start_new_thread(self.__update,())

      #parameters of OMNIKEY Cardman 5321
      readername = "OMNIKEY CardMan 5x21-CL 0"
      hardware = "PN531"
      supportProtocols = ('ISO15693','ISO14443A/B')
      supportTagTypes = ('Mifare Ultralight','Mifare 1K','Mifare 4K','TagIT')

      #tag status
      hasAnOldTag = False
      tagTouched = False
      tagRemoved = False
      lock = threading.Lock()
      
      
      def isTagConnected(self):
          #self.lock.acquire()
          if self.tagTouched:
                #self.lock.release()
                self.tagTouched = False
                self.hasAnOldTag = True
                return True
          else:
                #self.lock.release()
                return False

      def isTagReleased(self):
          #self.lock.acquire()
          if self.tagRemoved:
                #self.lock.release()
                self.tagRemoved = False
                self.hasAnOldTag = False
                return True
          else:
                #self.lock.release()
                return False

      def __update(self):
          while True:
                state = self.pollForATag()
                #self.lock.acquire()
                #update tagTouched,tagRemoved
                if self.hasAnOldTag:
                     if state:
                            self.tagTouched = False
                            self.tagRemoved = False
                     else:
                            self.tagTouched = False
                            self.tagRemoved = True
                else:
                     if state:
                            self.tagTouched = True
                            self.tagRemoved = False
                     else:
                            self.tagTouched = False
                            self.tagRemoved = False
                #self.lock.release()

      def getConnectedTag(self):
          pass

      def getReaderInfo(self):
          return self.readerInfo

      def kill(self):
          thread.exit()
          del self

#self-testing
if __name__ == '__main__':
    print "The program will exit if there is no tag action for 30secs"
    time0 = time.time()
    omi = OMNIKEY_Cardman5321(readers()[1])
    while time.time()-time0 < 30:
              if omi.isTagConnected():
                    print "tag connect"
              if omi.isTagReleased():
                    print "tag remove"
    omi.kill()
          
