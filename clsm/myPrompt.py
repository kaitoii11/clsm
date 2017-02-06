#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cmd import Cmd
from clsm.modelwrapper import ModelWrapper
import readline
import dircache

class MyPrompt(Cmd):
    prompt = '>'
    readline.parse_and_bind('tab: complete')

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
        elements = self.modelWrapper.getListOfAllElements()
        if text:
            return [i.getId() for i in elements if i.isSetId() and i.getId().startswith(text)] + filter(lambda n: n.startswith(text), printcompletion)
        else:
            return [i.getId() for i in elements if i.isSetId()] + printcompletion

    def do_create(self, line):
        line = line.split()
        if len(line) < 2:
            self.help_create()
            return
        sbasetype = line[0]
        sbaselist = line[1:]
        for sid in sbaselist:
            self.modelWrapper.createSBase(sbasetype, sid)

    def help_create(self):
        print 'help create'

    def complete_create(self, text, lie, start_idx, end_idx):
        if text:
            return filter(lambda n: n.startswith(text), printcompletion)
        else:
            return printcompletion

    def do_remove(self, line):
        line = line.split()
        if len(line) < 1:
            self.help_remove()
            return

        for sid in line:
            self.modelWrapper.removeSBase(sid)

    def help_remove(self):
        print 'help remove'

    def complete_remove(self, text, line, start_idx, end_idx):
        elements = self.modelWrapper.getListOfAllElements()
        if text:
            return [i.getId() for i in elements if i.isSetId() and i.getId().startswith(text)]
        else:
            return [i.getId() for i in elements if i.isSetId()]

    def do_write(self, line):
        line = line.split()
        if len(line) < 1:
            self.help_write()
            return
        else:
            for path in line:
                self.modelWrapper.write(path)

    def help_write(self):
        print 'write help'

    def complete_write(self, text, line, start_idx, end_idx):
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
        ls = filter(lambda n: n.endswith('/'),ls)
        if filename == '':
            return ls
        else:
            return [f for f in ls if f.startswith(filename)]


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
