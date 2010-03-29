#!/usr/bin/python
#ReaderTagManager.py

from ACS_ACU122 import ACS_ACU122
from OMNIKEY_CARDMAN5321 import OMNIKEY_Cardman5321
from pcsc_reader import PCSC_Reader
from RTMEvent import RTMevent
from smartcard.System import *
from smartcard.util import *
import string
import threading,thread
import time

class readerTagManager:

   def __init__(self):
       thread.start_new_thread(self.__update,())

   #key - pcsc reader name, map to pcsc reader instance
   pcsc_readerDictionary = {}
   #key - reader name, map to abstractReader instance
   readerDictionary = {}
   addInDictionary = {}
   #move out list
   moveOutList = []
   #tag
   tag = None
   #event list
   rtmEventList = []
   newEventNum = 0
   lock = threading.Lock()

   def __update(self):
       while True:
           self.lock.acquire()
           self.__updateReaderLists()
           self.__updateEventList()
           self.lock.release()
       #update every 0.5secs
           time.sleep(0.5)

   def __updateReaderLists(self):
       #clear pcsc reader list
       self.pcsc_readerDictionary.clear()
       #get pcsc reader list
       try:
          r = readers()
       except:
          r = []
       for reader in r:
           self.pcsc_readerDictionary[reader.name] = reader
       #get other readers using different APIs

       #--------------------------------------
       for key in self.pcsc_readerDictionary.keys():
            if not key in self.readerDictionary.keys():
                if string.find(key,'    CCID USB Reader') == 0:
                   acs = ACS_ACU122(self.pcsc_readerDictionary[key])
                   self.addInDictionary[key] = acs
                elif string.find(key,'OMNIKEY CardMan 5x21-CL') == 0:
                   omi = OMNIKEY_Cardman5321(self.pcsc_readerDictionary[key])
                   self.addInDictionary[key] = omi
                else:
                   unknown_pcsc_reader = PCSC_Reader(self.pcsc_readerDictionary[key])
                   self.addInDictionary[key] = unknown_pcsc_reader

       for key in self.readerDictionary.keys():
            if not key in self.pcsc_readerDictionary.keys():
                self.moveOutList.append(key)

       #get current reader list according to the add in readers and move out readers
       for key in self.addInDictionary.keys():
           self.readerDictionary[key] = self.addInDictionary[key]
       for reader in self.moveOutList:
           del self.readerDictionary[reader]
       #----------------------------------------------------------------------------
          
      
   def __updateEventList(self):
       if len(self.addInDictionary.keys()) > 0:
           self.newEventNum += 1
           #make a local list of the global variable addInList
           addInList = []
           for key in self.addInDictionary.keys():
               addInList.append(self.addInDictionary[key])
           self.rtmEventList.append(RTMevent("Reader is plugin",addInList,[],[],[]))
           self.addInDictionary.clear()
       if len(self.moveOutList) > 0:
           self.newEventNum += 1
           #make a local copy of the global variable moveOutList
           moveOutList = []
           for reader in self.moveOutList:
               moveOutList.append(reader)
           self.rtmEventList.append(RTMevent("Reader is removed",[],moveOutList,[],[]))
           del self.moveOutList[:]
       #update Reader status
       for key in self.readerDictionary.keys():
          #if the reader is recognized by the API but not for our application
          #skip that reader and check the next one
          if self.readerDictionary[key].__class__ == PCSC_Reader:
             continue
          self.readerDictionary[key].update()
          if self.readerDictionary[key].isTagConnected():
             self.tag = self.readerDictionary[key].getConnectedTag()
             self.rtmEventList.append(RTMevent("Tag is attached",[],[],self.tag,[]))
             self.newEventNum += 1
          if self.readerDictionary[key].isTagReleased():
             self.tag = None
             self.rtmEventList.append(RTMevent("Tag is removed",[],[],[],[]))
             self.newEventNum += 1
       #other events
       #------------

   def getReaderList(self):
       self.lock.acquire()
       readerlist = []
       for readername in self.readerDictionary.keys():
           readerlist.append(self.readerDictionary[readername])
       self.lock.release()
       return readerlist

#   def getReaderInUse(self,readername):
#       return self.readerDictionary[readername]

   def getTag(self):
       return self.tag

   def getReaderInUse(self,readername):
       return self.readerDictionary[readername]



   def hasNewEvent(self):
       #check if there are still events that not yet be got
       self.lock.acquire()
       if self.newEventNum > 0:
           self.lock.release()
           return True
       else:
           self.lock.release()
           return False



   def getNewEvent(self):
       self.lock.acquire()
       self.newEventNum -= 1
       event = self.rtmEventList[0]
       del self.rtmEventList[0]
       self.lock.release()
       return event




#self-testing
if __name__ == '__main__':
       rtm = readerTagManager()
       while True:
           time.sleep(1)
           if rtm.hasNewEvent():
                rtmevent = rtm.getNewEvent()
                print rtmevent.getEventType()
