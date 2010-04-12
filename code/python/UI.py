#!/usr/bin/python
#ui.py
from smartcard.util import *
from UIEvent import UIevent
from database import *
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

   def printNewReaderInfo(self,reader):
       self.printRTMEventDashLine()
       print "Reader detected:", reader.getReaderInfo().getCurrentReaderName(),
       self.printRTMEventDashLine()
       self.printCmdPrompt()

   def printRemovedReaderInfo(self,reader):
       self.printRTMEventDashLine()
       print "Reader removed:", reader
       self.printRTMEventDashLine()
       self.printCmdPrompt()

   def printNewTagInfo(self,tag):
       self.printRTMEventDashLine()
       print "New tag found:"
       if tag != None: 
           print "tagType: "+tag.getTagInfo().getTagType()
           print "UID: " + tag.getTagInfo().getTagUID()
           print "ATR: " + tag.getTagInfo().getATR()
           print "Manufacturer: " + tag.getTagInfo().getManufacturerInfo()
           if tag.getTagInfo().getIsAPDUSupported():
              print "APDU supportable : Yes",
           else:
              print "APDU supportable : No",
       else: print 'error: None-tag in UI.'
       self.printRTMEventDashLine()
       self.printCmdPrompt()

   def printRemovedTagInfo(self):
       self.printRTMEventDashLine()
       print "Tag is removed!",
       self.printRTMEventDashLine()
       self.printCmdPrompt()
       

   def printModeSwitchInfo(self,flag):
       if flag:
          print "Warning!Switched to the expert mode."
       else:
          print "Warning!Switched to the normal user mode."

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

   def printTagExternalTools(self,tagName,toolList):
       if len(toolList) == 0:
           print "Haven't found any tool can be used for tag %s" % tagName
       else:   
           print "The following external tools may be available For tag %s:" % tagName 
           for tool in toolList:
               print "%s " % tool,
           print ''
      
   def printOutOfRange(self):
       print "There is no such reader connected to computer, please type list to see the details."

   def printDoesntSupportAPDU(self):
       print "Sorry, this type of tag doesn't support APDU."

   def printNoReader(self):
       print "No reader present!"

   def printNoTag(self):
       print "No tag is available!"

   def printMifareUltralight(self,data):
       print ''
       count = 0
       for line in data:
          print "Block %02x:    %s" % (count,toHexString(line))
          count += 1

   def printNeedToSelectReader(self):
       print "Please select a reader!"
        
   def printShowNormalUserOptions(self):
       print "\n---------------------------------------------------------"
       print "help----------------------------get normal user help text"
       print "list------list out all the readers and tags in the system"
       print "tag?-----------find out possible readers can read the tag"
       print "readtag-------------------------reads out data in the tag"
       print "tool----------------show available external tools for tag"
       print "sel #---------------------------------select reader num #"
       print "apdu -------------------------------------enter apdu mode"
       print "exit-------------------------------------exit the program"

   def printShowExpertUserOptions(self):
       print "\n---------------------------------------------------------"
       print "help----------------------------get expert user help text"
       print "normal-----------------------back to the normal user mode"
       print "please enter apdu as the following format(hex):          "
       print "eg.ff ca 00 00 00(No space at the end)                   "

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
                     print "     ATR: "+tag.getTagInfo().getATR()
                     print "     Manufacturer: "+ tag.getTagInfo().getManufacturerInfo()
                     if tag.getTagInfo().getIsAPDUSupported():
                               print "     APDU supportable : Yes"
                     else:
                               print "     APDU supportable : No"
               else: print 'error: none-tag in UI.py'

   def printRTMEventDashLine(self):
       print "\n*************************************************************"
                  
   @staticmethod
   def printReturnedAPDU(data,sw1,sw2):
       print "data: "
       print toHexString(data)
       print "status byte: %02x %02x" % (sw1,sw2)


   def printSolutionForUnknownTag(self,taglist):
       if len(taglist) == 0:
          print "Sorry, our software doesn't support reading of the tag with this type\n"
       else:
          print "The tag connected might be the following types:"
          for tag in taglist:
             print "%s " % tag

   def printUnImplementedTag(self,readername):
       print "The tag is recognized by %s but we haven't implement the tag for this reader, sorry for that." % readername

   def printUnrecognizedAPDUCommand(self):
       print "Sorry, this reader doesn't support this kind of APDU. "

   def printUnknownCommand(self):
       print "\n---------------------------------------------------------------------------------"
       print "The command is unknown, please re-input and if any doubt please type help command"

   def printCmdPrompt(self):
         print "Please type in command:",

   def printTagIsRecognized(self,tag,reader):
         print "The tag type is %s and it is connected to reader %s" % (tag,reader)

   def clearEventFlag(self):
         self.eventFromUI.clear()

   def setEventFlag(self):
         self.eventFromUI.set()
         
if __name__ == '__main__':
   ui = userInterface()
   while True:
       if ui.hasNewEvent():
           ui.getNewEvent()
