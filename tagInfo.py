#!/usr/bin/python
#tagInfo.py

class tagInfo:

    def __init__(self,tagType,UID,supportProtocol,supportExternalTools,manufacturer,corresponseReader):
        self.tagType = tagType
        self.UID = UID
        self.supportProtocol = supportProtocol
        self.supportExternalTools = supportExternalTools
        self.manufacturer = manufacturer
        self.corresponseReader = corresponseReader

    def getTagType(self):
        return self.tagType

    def getTagUID(self):
        return self.UID

    def getSupportProtocol(self):
        return self.supportProtocol

    def getSupportExternalTools(self):
        return self.supportExternalTools

    def getManufacturerInfo(self):
        return self.manufacturer

    def getCorresponseReader(self):
        return self.corresponseReader
