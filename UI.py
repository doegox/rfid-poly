#!/usr/bin/python
#UI.py

from UIEvent import UIevent
import threading
import thread
import time

class userInterface:

   def __init__(self):
       self.eventFromUI.set()
       thread.start_new_thread(self.__checkNewEvent,())

   newEventNum = 0
   newEventList = []
   programExit = False
   eventFromUI = threading.Event()

   def __checkNewEvent(self):
       while True:
           if self.newEventNum == 0:
                          self.eventFromUI.wait()
                          if not self.programExit:
                              self.printCmdPrompt()
                              cmd = str(raw_input(""))
                              self.newEventList.append(UIevent(cmd))
                              self.newEventNum += 1
                              if cmd == 'exit':
                                  self.programExit = True

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
           print reader.getReaderInfo().getCurrentReaderName()
       self.printCmdPrompt()

   def printRemovedReaderInfo(self,readerlist):
       print "\n-----------new events------------"
       print "EventType: Some readers are removed"
       print "Software detected the following readers are removed:"
       for reader in readerlist:
           print reader
       self.printCmdPrompt()

   def printNewTagInfo(self,tag):
       print "\n-----------new events------------"
       print "EventType: New tag is found!"
       print "Software detected the following tags are new added:"
       print "tagType: "+tag.getTagInfo().getTagType()
       print "UID: " + tag.getTagInfo().getTagUID()
       print "Manufacturer: " + tag.getTagInfo().getManufacturerInfo()
       self.printCmdPrompt()

   def printRemovedTagInfo(self):
       print "\n-----------new events------------"
       print "EventType: Tag is removed!"
       self.printCmdPrompt()

   def printSelectReaderInfo(self,reader):
       print "\n---------------------------------"
       print reader.getReaderInfo().getCurrentReaderName() + "is selected!"
       print "The returned reader info: "
       print "ReaderName: "+reader.getReaderInfo().getName()+"\n"
       print "Hardware inside chip: "+reader.getReaderInfo().getHardware()+"\n"
       print "Reader supports following protocols: "
       if reader.getReaderInfo().getName() != "Unknown":
           for i in reader.getReaderInfo().getSupportProtocols():
                  print i
       else:
           print "Unknown"
       print "\n"
       print "Reader supports following tags:"
       if reader.getReaderInfo().getName() != "Unknown":
           for j in reader.getReaderInfo().getSupportTagTypes():
                  print j
       else:
           print "Unknown"
       print "\n"

   def printOutOfRange(self):
       print "There is no such reader connected to computer, please type list to see the details."
       
   def printShowOptions(self):
       print "\n---------------------------------------------------------"
       print "help----------------------------------------get help text"
       print "list------list out all the readers and tags in the system"
       print "sel #---------------------------------select reader num #"
       print "exit-------------------------------------exit the program"

   def printDeviceList(self,readerlist,tag):
       print "\n---------------------------------------------------"
       if len(readerlist) == 0:
           print "No readers are connected!"
       else:
           print "The following devices are detected by our software:"
           count = 1
           for reader in readerlist:
               print "#%i :%s" % (count,reader.getReaderInfo().getCurrentReaderName())
               count += 1
               if tag != None:
                  if tag.getTagInfo().getCorresponseReader() == reader.getReaderInfo().getCurrentReaderName():
                     print "     with tag:"
                     print "     tagType: "+tag.getTagInfo().getTagType()
                     print "     UID: "+tag.getTagInfo().getTagUID()
                     print "     Manufacturer: "+ tag.getTagInfo().getManufacturerInfo()

   def printUnknownCommand(self):
       print "\n---------------------------------------------------------------------------------"
       print "The command is unknown, please re-input and if any doubt please type help command"

   def printCmdPrompt(self):
         print "Please type in command:"

   def clearEventFlag(self):
         self.eventFromUI.clear()

   def setEventFlag(self):
         self.eventFromUI.set()
         
if __name__ == '__main__':
   ui = userInterface()
   while True:
       if ui.hasNewEvent():
           ui.getNewEvent()