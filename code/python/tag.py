#!/usr/bin/python
#tag.py
#abstract class of tag

class abstractTag:
      def __init__(self):
          if self.__class__ == abstractTag:
              raise NotImplementedError,"Cannot create object of class abstractTag"

      def getTagInfo(self):
          raise NotImplementedError,"Cannot call abstract method"

