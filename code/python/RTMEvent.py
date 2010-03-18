from reader import abstractReader

class RTMevent:

    def __init__(self,eventType,eventAddData,eventRemoveData):
        self.eventType = eventType
        self.eventAddData = eventAddData
        self.eventRemoveData = eventRemoveData

    def getEventType(self):
        return self.eventType

    def getEventAddData(self):
        return self.eventAddData

    def getEventRemoveData(self):
        return self.eventRemoveData
