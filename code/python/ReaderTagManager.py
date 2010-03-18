from ACS_ACU122 import ACS_ACU122
from OMNIKEY_CARDMAN5321 import OMNIKEY_Cardman5321
from RTMEvent import RTMevent
from smartcard.System import *
from smartcard.util import *
import string
import time

class readerTagManager:

    def __init__(self):
        pass

    #key - pcsc reader name, map to pcsc reader instance
    pcsc_readerDictionary = {}
    #key - reader name, map to abstractReader instance
    readerDictionary = {}
    addInDictionary = {}
    #move out list
    moveOutList = []
    #event list
    rtmEventList = []
    newEventNum = 0


    def getReaderList(self):
        #clear pcsc reader list
        self.pcsc_readerDictionary.clear()
        #get pcsc reader list
        r = readers()
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
                    pass
                
        for key in self.readerDictionary.keys():
             if not key in self.pcsc_readerDictionary.keys():
                 self.moveOutList.append(key)

        #get current reader list according to the add in readers and move out readers
        for key in self.addInDictionary.keys():
            self.readerDictionary[key] = self.addInDictionary[key]
        for reader in self.moveOutList:
            del self.readerDictionary[reader]

        
                
    def hasNewEvent(self):
        #check if there are still events that not yet be got
        if self.newEventNum > 0:
            return True
        self.getReaderList()
        if len(self.addInDictionary.keys()) > 0:
            self.newEventNum += 1
            #make a local list of the global variable addInList
            addInList = []
            for key in self.addInDictionary.keys():
                addInList.append(self.addInDictionary[key])
            self.rtmEventList.append(RTMevent("Reader is plugin",addInList,[]))
            self.addInDictionary.clear()
        if len(self.moveOutList) > 0:
            self.newEventNum += 1
            #make a local copy of the global variable moveOutList
            moveOutList = []
            for reader in self.moveOutList:
                moveOutList.append(reader)
            self.rtmEventList.append(RTMevent("Reader is removed",[],moveOutList))
            del self.moveOutList[:]
        #other events
        #------------
        if self.newEventNum > 0:
            return True
        else:
            return False
        
        
        
    def getNewEvent(self):
        self.newEventNum -= 1
        event = self.rtmEventList[0]
        del self.rtmEventList[0]
        return event
        


        
#self-testing        
if __name__ == '__main__':
        rtm = readerTagManager()
        while True:
            if rtm.hasNewEvent():
                 rtmevent = rtm.getNewEvent()
                 print rtmevent.getEventType()
                 print rtmevent.getEventAddData()
                 print rtmevent.getEventRemoveData()
            time.sleep(1)
            
