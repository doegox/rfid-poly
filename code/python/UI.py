from UIEvent import UIevent
import threading,thread
import time

class userInterface:

    def __init__(self):
        thread.start_new_thread(self.__checkNewEvent,())

    newEventNum = 0
    newEventList = []

    def __checkNewEvent(self):
        while True:
            if self.newEventNum == 0:
               time.sleep(1)
               cmd = str(raw_input("Please type in command:"))
               self.newEventList.append(UIevent(cmd))
               self.newEventNum += 1

    def hasNewEvent(self):
        if self.newEventNum > 0:
            return True
        else:
            return False

    def getNewEvent(self):
        uievent = self.newEventList[0]
        del self.newEventList[0]
        self.newEventNum -= 1
        return uievent

    def printNewReaderInfo(self,readerlist):
        print "\n-----------new events------------"
        print "EventType: New readers are plugin"
        print "Software detected the following readers are new added:"
        for reader in readerlist:
            print reader.getReaderInfo().getName()

    def printRemovedReaderInfo(self,readerlist):
        print "\n-----------new events------------"
        print "EventType: Some readers are removed"
        print "Software detected the following readers are removed:"
        for reader in readerlist:
            print reader

    def printShowOptions(self):
        print "\n---------------------------------------------------------"
        print "help----------------------------------------get help text"
        print "list---------------list out all the readers in the system"
        print "exit-------------------------------------exit the program"

    def printReaderList(self,readerlist):
        print "\n---------------------------------------------------"
        if len(readerlist) == 0:
            print "No readers are connected!"
        else:
            print "The following readers are detected by our software:"
            for reader in readerlist:
                print reader.getReaderInfo().getName()

    def printUnknownCommand(self):
        print "\n---------------------------------------------------------------------------------"
        print "The command is unknown, please re-input and if any doubt please type help command"

    def printReminder(self):
        print "Please type in command:"

if __name__ == '__main__':
    ui = userInterface()
    while True:
        if ui.hasNewEvent():
            ui.getNewEvent()
