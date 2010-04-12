#!usr/bin/python
#UIEvent.py

class UIevent:

   def __init__(self,cmd):
       self.cmd = cmd

   def getCommand(self):
       return self.cmd.lower()
