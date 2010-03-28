#!/usr/bin/python
#RTMEvent.py

from reader import abstractReader

class RTMevent:

   def __init__(self,eventType,readerAddData,readerRemoveData,tagAddData,tagRemoveData):
       self.eventType = eventType
       self.readerAddData = readerAddData
       self.readerRemoveData = readerRemoveData
       self.tagAddData = tagAddData
       self.tagRemoveData = tagRemoveData

   def getEventType(self):
       return self.eventType

   def getReaderAddData(self):
       return self.readerAddData

   def getReaderRemoveData(self):
       return self.readerRemoveData

   def getTagAddData(self):
       return self.tagAddData

   def getTagRemoveData(self):
       return self.tagRemoveData
