# -*- coding: utf-8 -*-

from cmd import Cmd

class myPrompt(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = '>'

#if __name__ = '__main__':
#    prompt = myPrompt()
#    prompt.cmdloop()
