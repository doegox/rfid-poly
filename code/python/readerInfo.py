class readerInfo:

    def __init__(self,readerName,hardware,supportProtocols,supportTagTypes):
        self.readerName = readerName
        self.hardware = hardware
        self.supportProtocols = supportProtocols
        self.supportTagTypes = supportTagTypes

    def getName(self):
        return self.readerName

    def getHardware(self):
        return self.hardware

    def getSupportProtocols(self):
        return self.supportProtocols

    def getSupportTagTypes(self):
        return self.supportTagTypes

    def printOutInfo(self):
        print "ReaderName: "+self.readerName+"\n"
        print "Hardware inside chip: "+self.hardware+"\n"
        print "Reader supports following protocols: "
        for i in self.supportProtocols:
            print i
        print "\n"
        print "Reader supports following tags:"
        for j in self.supportTagTypes:
            print j
        print "\n"
