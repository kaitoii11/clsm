#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cmd import Cmd

class myPrompt(Cmd):
    prompt = '>'
    def __init__(self, modelWrapper):
        Cmd.__init__(self)
        self.modelWrapper = modelWrapper

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass
