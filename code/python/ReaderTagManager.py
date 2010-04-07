#!/usr/bin/python
#ReaderTagManager.py

from ACS_ACU122 import ACS_ACU122
from OMNIKEY_CARDMAN5321 import OMNIKEY_Cardman5321
from pcsc_reader import PCSC_Reader
from RTMEvent import *
from smartcard.System import *
from smartcard.util import *
import string
import os
import threading,thread
import time

class readerTagManager:

   def __init__(self):
       thread.start_new_thread(self.__update,())
       
   r = []
   #key - pcsc reader name, map to pcsc reader instance
   pcsc_readerDictionary = {}
   #key - reader name, map to abstractReader instance
   readerDictionary = {}
   addInDictionary = {}
   moveOutList = []
   tag = None
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
            print 'error. not sure what to do ... '
       for reader in r:
           self.pcsc_readerDictionary[reader.name] = reader
       #get other readers using different APIs

       #--------------------------------------
       for key in self.pcsc_readerDictionary.keys():
            if not key in self.readerDictionary.keys():    
                if ACS_ACU122.isThisType(os.name,key):
                   new_reader = ACS_ACU122(self.pcsc_readerDictionary[key])
                elif OMNIKEY_Cardman5321.isThisType(os.name,key):
                   new_reader = OMNIKEY_Cardman5321(self.pcsc_readerDictionary[key])
                else:
                   new_reader = PCSC_Reader(self.pcsc_readerDictionary[key])
                self.addInDictionary[key] = new_reader

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
           #make a local list of the global variable addInList
           for key in self.addInDictionary.keys():
               self.newEventNum += 1
               self.rtmEventList.append(RTMevent(RTMET_READER_DETECTED,self.addInDictionary[key]))
           self.addInDictionary.clear()
       if len(self.moveOutList) > 0:
           #make a local copy of the global variable moveOutList
           for reader in self.moveOutList:
               self.rtmEventList.append(RTMevent(RTMET_READER_REMOVED,reader))
               self.newEventNum += 1
           del self.moveOutList[:]
       #update Reader status
       for key in self.readerDictionary.keys():
          #if the reader is recognized by the API but not for our application
          #skip that reader and check the next one
          #if self.readerDictionary[key].__class__ == PCSC_Reader:
          #   continue
          self.readerDictionary[key].update()
          if self.readerDictionary[key].isTagConnected():
             self.tag = self.readerDictionary[key].getConnectedTag()
             self.rtmEventList.append(RTMevent(RTMET_TAG_DETECTED,self.tag))
             self.newEventNum += 1
          if self.readerDictionary[key].isTagReleased():
             self.tag = None
             self.rtmEventList.append(RTMevent(RTMET_TAG_REMOVED,None))
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



#self-testing : what does it do??
if __name__ == '__main__':
       rtm = readerTagManager()
       while True:
           time.sleep(1)
           if rtm.hasNewEvent():
                rtmevent = rtm.getNewEvent()
                print rtmevent.getEventType()
