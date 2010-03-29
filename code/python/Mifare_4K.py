#!/usr/bin/python
#Mifare_Ultralight.py
from tag import abstractTag
from tagInfo import tagInfo

class Mifare_4K(abstractTag):

      def __init__(self,UID,corresponseReader):
          abstractTag.__init__(self)
          self.UID = UID
          self.corresponseReader = corresponseReader

      tagType = "Mifare Classic 4K"
      supportProtocol = "ISO14443"
      supportExternalTools = ("cardselect.py","isotype.py","readmifaresimple.py")
      manufacturer = "NXP"
      isAPDUSupported = True

      def getTagInfo(self):
          return tagInfo(self.tagType,self.UID,self.supportProtocol,self.supportExternalTools,self.manufacturer,self.corresponseReader,self.isAPDUSupported)
