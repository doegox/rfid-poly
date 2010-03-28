#!/usr/bin/python
#Mifare_Ultralight.py
from tag import abstractTag
from tagInfo import tagInfo

class Mifare_Ultralight(abstractTag):

      def __init__(self,UID,corresponseReader):
          abstractTag.__init__(self)
          self.UID = UID
          self.corresponseReader = corresponseReader

      tagType = "Mifare Ultralight"
      supportProtocol = "ISO14443"
      supportExternalTools = ("readtag.py","isotype.py","readmifareultra.py")
      manufacturer = "NXP"

      def getTagInfo(self):
          return tagInfo(self.tagType,self.UID,self.supportProtocol,self.supportExternalTools,self.manufacturer,self.corresponseReader)
        
