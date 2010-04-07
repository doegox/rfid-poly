#!/usr/bin/python
#Mifare_Ultralight.py
from tag import abstractTag
from tagInfo import tagInfo
from database import *

class Mifare_4K(abstractTag):

      def __init__(self,UID,corresponseReader):
          abstractTag.__init__(self)
          self.UID = UID
          self.corresponseReader = corresponseReader

      tagType = MIFARE_4K
      supportProtocol = ISO14443
      supportExternalTools = (CARDSELECT,ISOTYPE,READMIFARESIMPLE)
      manufacturer = "NXP"
      isAPDUSupported = True

      def getTagInfo(self):
          return tagInfo(self.tagType,self.UID,self.supportProtocol,self.supportExternalTools,self.manufacturer,self.corresponseReader,self.isAPDUSupported)
