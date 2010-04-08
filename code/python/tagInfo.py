#!/usr/bin/python
#tagInfo.py

class tagInfo:

    def __init__(self,tagType,UID,ATR,supportProtocol,supportExternalTools,manufacturer,corresponseReader,isAPDUSupported):
        self.tagType = tagType
        self.UID = UID
        self.ATR = ATR
        self.supportProtocol = supportProtocol
        self.supportExternalTools = supportExternalTools
        self.manufacturer = manufacturer
        self.corresponseReader = corresponseReader
        self.isAPDUSupported = isAPDUSupported

    def getTagType(self):
        return self.tagType

    def getTagUID(self):
        return self.UID

    def getATR(self):
        return self.ATR
    
    def getSupportProtocol(self):
        return self.supportProtocol

    def getSupportExternalTools(self):
        return self.supportExternalTools

    def getManufacturerInfo(self):
        return self.manufacturer

    def getCorresponseReader(self):
        return self.corresponseReader

    def getIsAPDUSupported(self):
        return self.isAPDUSupported
