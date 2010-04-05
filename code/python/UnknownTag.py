#!/usr/bin/python
#UnknownTag.py
from tag import abstractTag
from tagInfo import tagInfo

class UnknownTag(abstractTag):

      def __init__(self,UID,corresponseReader):
          abstractTag.__init__(self)
          self.UID = UID
          self.corresponseReader = corresponseReader

      tagType = "Unknown"
      supportProtocol = "Unknown"
      supportExternalTools = ("")
      manufacturer = "Unknown"
      isAPDUSupported = False

      def getTagInfo(self):
          return tagInfo(self.tagType,self.UID,self.supportProtocol,self.supportExternalTools,self.manufacturer,self.corresponseReader,self.isAPDUSupported)
        