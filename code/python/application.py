#!/usr/bin/python#application.pyfrom ReaderTagManager import readerTagManagerfrom UI import userInterfacefrom reader import abstractReaderfrom dataHandler import *from RTMEvent import *import stringimport timertm = readerTagManager()ui = userInterface()readerlist = []reader = Nonetag = NonenormalUserMode = TrueAPDUConsoleMode = FalseuserTypeExit = Falsewhile not userTypeExit:   if rtm.hasNewEvent():       rtmevent = rtm.getNewEvent()       readerlist = rtm.getReaderList()       tag = rtm.getTag()       if rtmevent.getEventType() == RTMET_READER_DETECTED:           ui.printNewReaderInfo(rtmevent.getReaderAddData())       elif rtmevent.getEventType() == RTMET_READER_REMOVED:           ui.printRemovedReaderInfo(rtmevent.getReaderRemoveData())       elif rtmevent.getEventType() == RTMET_TAG_DETECTED:           ui.printNewTagInfo(rtmevent.getTagAddData())       elif rtmevent.getEventType() == RTMET_TAG_REMOVED:           ui.printRemovedTagInfo()       else:           assert(False)              if ui.hasNewEvent():       ui.clearEventFlag()       cmd = ui.getNewEvent().getCommand()       if normalUserMode:           if cmd == 'help':              ui.printShowNormalUserOptions()           elif cmd == 'list':              ui.printDeviceList(readerlist,tag)           elif cmd == 'readtag':              if tag == None:                 ui.printNoTag()              else:                 if tag.getTagInfo().getTagType() == 'Mifare Ultralight':                       for one in readerlist:                          if one.getReaderInfo().getCurrentReaderName() == tag.getTagInfo().getCorresponseReader():                                    ui.printMifareUltralight(one.readMifareUltralight())           elif string.find(cmd,'sel ') == 0:                if len(readerlist) < findNumberInString(cmd) or findNumberInString(cmd) <= 0:                   ui.printOutOfRange()                else:                   reader = readerlist[findNumberInString(cmd)-1]                   ui.printSelectReaderInfo(readerlist[findNumberInString(cmd)-1])           elif cmd == 'exit':                   userTypeExit = True           elif cmd == '':                pass           elif cmd == 'apdu':              if len(readerlist) != 0:                  if reader == None:                      ui.printNeedToSelectReader()                  else:                      ui.printModeSwitchInfo(normalUserMode)                      reader.enterAPDU()                      normalUserMode = False                      APDUConsoleMode = True              else:                 ui.printNoReader()           else:                ui.printUnknownCommand()       elif APDUConsoleMode:           if cmd == 'normal':              ui.printModeSwitchInfo(normalUserMode)              reader.backToNormal()              normalUserMode = True              APDUConsoleMode = False           elif cmd == 'help':              ui.printShowExpertUserOptions()           elif cmd == '':              pass           else:                 if stringToArray(cmd) != None:                    result,sw1,sw2 = reader.transmitAPDU(stringToArray(cmd))                    ui.printReturnedAPDU(result,sw1,sw2)                 else:                    ui.printUnrecognizedAPDUCommand()       else:           assert(1/0)       ui.setEventFlag()         