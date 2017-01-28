#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages/libsbml")
from libsbml import *

class modelWrapper:
    def __init__(self, src=None, dst='output.xml'):
        if(src == None):
            self.__createDocument()
        else:
            self.document = readSBML(src)
            self.model = document.getModel()

        self.dst = dst

    def __createDocument(self):
        self.document = SBMLDocument()
        self.model = self.document.createModel()

    @staticmethod
    def createModelWrapper(**kwargs):
        return modelWrapper(**kwargs)
