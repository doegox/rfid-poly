#!/usr/bin/python
#Mifare_Desfire.py
from tag import abstractTag
from tagInfo import tagInfo
from database import *

class Mifare_Desfire(abstractTag):

      def __init__(self,UID,ATR,corresponseReader):
          abstractTag.__init__(self)
          self.UID = UID
          self.ATR = ATR
          self.corresponseReader = corresponseReader

      tagType = MIFARE_DESFIRE
      supportProtocol = ISO14443
      supportExternalTools = ()
      manufacturer = "NXP"
      isAPDUSupported = True

      def getTagInfo(self):
          return tagInfo(self.tagType,self.UID,self.ATR,self.supportProtocol,self.supportExternalTools,self.manufacturer,self.corresponseReader,self.isAPDUSupported)
        
