#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cmd import Cmd
from clsm.modelwrapper import ModelWrapper
import readline

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

    def do_print(self, line):
        line = line.split()
        if len(line) == 0:
            self.modelWrapper.printAttribute()
        else:
            self.modelWrapper.printAttribute(target=line)

    def help_print(self):
        print "print help"

    def do_exit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass
