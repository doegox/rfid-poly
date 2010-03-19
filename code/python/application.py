from ReaderTagManager import readerTagManager
from UI import userInterface
from reader import abstractReader

rtm = readerTagManager()
ui = userInterface()

userTypeExit = False

while not userTypeExit:
    if rtm.hasNewEvent():
        rtmevent = rtm.getNewEvent()
        if rtmevent.getEventType() == "Reader is plugin":
            ui.printNewReaderInfo(rtmevent.getEventAddData())
            ui.printReminder()
        elif rtmevent.getEventType() == "Reader is removed":
            ui.printRemovedReaderInfo(rtmevent.getEventRemoveData())
            ui.printReminder()
        else:
            pass
    if ui.hasNewEvent():
        cmd = ui.getNewEvent().getCommand()
        if cmd == 'help':
            ui.printShowOptions()
        elif cmd == 'list':
            ui.printReaderList(rtm.getReaderList())
        elif cmd == 'exit':
            userTypeExit = True
        else:
            ui.printUnknownCommand()



