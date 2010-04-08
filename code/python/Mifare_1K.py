#!/usr/bin/python
#Mifare_Ultralight.py
from tag import abstractTag
from tagInfo import tagInfo
from database import *

class Mifare_1K(abstractTag):

      def __init__(self,UID,ATR,corresponseReader):
          abstractTag.__init__(self)
          self.UID = UID
          self.ATR = ATR
          self.corresponseReader = corresponseReader

      tagType = MIFARE_1K
      supportProtocol = ISO14443
      supportExternalTools = (CARDSELECT,ISOTYPE,READMIFARE1K)
      manufacturer = "NXP"
      isAPDUSupported = True

      def getTagInfo(self):
          return tagInfo(self.tagType,self.UID,self.ATR,self.supportProtocol,self.supportExternalTools,self.manufacturer,self.corresponseReader,self.isAPDUSupported)
