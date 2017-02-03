#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cmd import Cmd
from clsm.modelwrapper import ModelWrapper
import readline
import dircache


class MyPrompt(Cmd):
    prompt = '>'
    readline.parse_and_bind ('tab: complete')

    def __init__(self, modelWrapper):
        Cmd.__init__(self)
        self.modelWrapper = modelWrapper

    def do_read(self, line):
        line = line.split()
        if len(line) < 1:
            self.help_read()
            return
        elif len(line) > 2:
            print "reading only the first argument"

        args = {'src': line[0]}
        self.modelWrapper = ModelWrapper.createModelWrapper(**args)

    def help_read(self):
        print "read help"

    # todo change dircache since it is deprecated in python3
    def complete_read(self, text, line, start_idx, end_idx):
        line = line.split()
        if len(line) < 2:
            filename = ''
            path = './'
        else:
            path = line[1]
            if '/' in path:
                i = path.rfind('/')
                filename = path[i+1:]
                path = path[:i]
            else:
                filename = path
                path = './'

        ls = dircache.listdir(path)
        ls = ls[:]
        dircache.annotate(path, ls)
        if filename == '':
            return ls
        else:
            return [f for f in ls if f.startswith(filename)]

    def do_print(self, line):
        line = line.split()
        if len(line) == 0:
            self.modelWrapper.printAttribute()
        else:
            self.modelWrapper.printAttribute(target=line)

    def help_print(self):
        print "print help"

    def complete_print(self, text, line, start_idx, end_idx):
        elements = self.modelWrapper.model.getListOfAllElements()
        if text:
            return [i.getId() for i in elements if i.isSetId() and i.getId().startswith(text)] + filter(lambda n: n.startswith(text), printcompletion)
        else:
            return [i.getId() for i in elements if i.isSetId()] + printcompletion

    def do_exit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

printcompletion = [
    'Species',
    'Reactions',
    'Compartments',
    'Rules',
    'Parameters',
    'UnitDefinitions',
    'Model',
    'Document',
]
