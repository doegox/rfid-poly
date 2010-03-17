from ACS_ACU122 import ACS_ACU122
from OMNIKEY_CARDMAN5321 import OMNIKEY_Cardman5321
from RTMEvent import RTMevent
from smartcard.System import *
from smartcard.util import *

class readerTagManager:

    def __init__(self):
        pass

    previousReaderList = []
    currentReaderList = []
    addInList = []
    moveOutList = []
    isReaderPlugin = False
    isReaderPlugout = False
    rtmEventList = []
    newEventNum = 0


    def getReaderList(self):
        #update
        self.previousReaderList = self.currentReaderList
        #re-get the current readerlist
        self.currentReaderList = []
        #get current ReaderList
        #PCSC_Reader
        for reader in readers():
            if string.find(reader.name,'    CCID USB Reader 0')==0:
                self.currentReaderList.append(ACS_ACU122(reader))
            elif string.find(reader.name,'OMNIKEY CardMan 5x21-CL 0')==0:
                self.currentReaderList.append(OMNIKEY_Cardman5321(reader))
            else:
                pass
        #readers using other APIs
        #....
            
        for reader in self.currentReaderList:
            if not reader in self.previousReaderList:
                self.addInList.append(reader)
        for reader in self.previousReaderList:
            if not reader in self.currentReaderList:
                self.moveOutList.append(reader)
        return self.currentReaderList
                

    def hasNewEvent(self):
        if self.newEventNum > 0:
            return True
        self.getReaderList()
        if self.isReaderPlugin:
            self.newEventNum = self.newEventNum + 1
            self.rtmEventList.append(RTMevent("Reader connected",addInList))
            self.isReaderPlugin = False
        if self.isReaderPlugout:
            self.newEventNum = self.newEventNum + 1
            self.rtmEventList.append(RTMevent("Reader removed",moveOutList))
            self.isReaderPlugout = False
        """for reader in self.currentReaderList:
            if reader.isTagConnected():
                self.newEventNum = self.newEventNum + 1
                self.rtmEventList.append(RTMevent("Tag connected",reader.getConnectedTag()))
            if reader.isTagReleased():
                self.newEventNum = self.newEventNum + 1
                self.rtmEventList.append(RTMevent("Tag released","")"""
        

    def getNewEvent(self):
        self.newEventNum = self.newEventNum - 1
        event = rtmEventList.pop()
        if event.
        
