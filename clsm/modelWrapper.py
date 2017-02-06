#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages/libsbml")
from libsbml import *

class ModelWrapper:
    def __init__(self, src=None, dst='output.xml'):
        if(src is None):
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

    def getListOfAllElements(self):
        return self.model.getListOfAllElements()

    def printAttribute(self, target=['document']):
        for i in target:
            if i == 'Document' or i.capitalize() == 'Document':
                print writeSBMLToString(self.document)
            elif i == 'Model' or i.capitalize() == 'Model' :
                print self.model.toSBML()
            elif hasattr(self.model, 'getListOf' + i.title()):
                print getattr(self.model, 'getListOf' + i.title())().toSBML()
            else:
                element = self.document.getElementBySId(i)
                if element is None:
                    print 'attribute ', i , ' not found'
                else:
                    print element.toSBML()

    def createSBase(self, sbasetype, sid):
        sbase = getattr(self.model, 'create' + sbasetype.capitalize())()
        sbase.setId(sid)

    def removeSBase(self, sid):
        sbase = self.model.getElementBySId(sid)
        if sbase is not None:
            getattr(self.model, 'remove' + sbase.__class__.__name__)(sid)

    def write(self, path):
        writeSBMLToFile(self.document, path)
