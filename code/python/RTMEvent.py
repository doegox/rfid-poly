#!/usr/bin/python
#RTMEvent.py

from reader import abstractReader


#-------------------------------------------------------------------------------
#allowed event types: 
LST_EVENT_TYPES = (
RTMET_READER_DETECTED, #data=reader instance
RTMET_READER_REMOVED, #data=reader string
RTMET_TAG_DETECTED, #data=tag instance
RTMET_TAG_REMOVED #data=None
) = range(4)


class RTMevent:
    def __init__(self, eventType, eventData):
       assert( eventType in LST_EVENT_TYPES )
       self.__eventType = eventType        
       self.__eventData = eventData

    def getEventType(self):
       return self.__eventType

    def getReaderAddData(self):
       assert( isinstance( self.__eventData, abstractReader) )
       return self.__eventData

    def getReaderRemoveData(self):
       assert ( type(self.__eventData) == str )
       return self.__eventData 

    def getTagAddData(self):
       return self.__eventData

    def getTagRemoveData(self):
       assert ( type(self.eventData) == type(None) )
       return self.__eventData


