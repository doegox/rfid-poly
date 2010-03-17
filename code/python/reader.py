#abstract class of reader


class abstractReader:

    def __init__(self):
        if self.__class__ == abstractReader:
           raise NotImplementedError,"Cannot create object of class abstractReader"

        
    def isTagConnected(self):
        raise NotImplementedError,"Cannot call abstract method"

    def isTagReleased(self):
        raise NotImplementedError,"Cannot call abtract method"

    def getReaderInfo(self):
        raise NotImplementedError,"Cannot call abstract method"
    
    def getConnectedTag(self):
        raise NotImplementedError,"Cannot call abstract method"



