#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages/libsbml")
from libsbml import *

class ModelWrapper:
    def __init__(self, src=None, dst='output.xml'):
        if(src == None):
            self.__createDocument()
        else:
            self.document = readSBML(src)
            self.model = self.document.getModel()

        self.dst = dst

    def __createDocument(self):
        self.document = SBMLDocument()
        self.model = self.document.createModel()

    @staticmethod
    def createModelWrapper(**kwargs):
        return ModelWrapper(**kwargs)

    def printAttribute(self, target=['document']):
        for i in target:
            if i == 'document':
                writeSBMLToString(self.document)
            elif i == 'model':
                writeSBMLToString(self.document.getModel())
            else:
                element = document.getElementBySId(i)
                if element  is None:
                    print 'attribute ', i , ' not found'
                else:
                    writeSBMLToString(i)
