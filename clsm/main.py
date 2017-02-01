#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
#from clsm import __version__ as VERSION
from clsm.modelwrapper import ModelWrapper

class clsmMain():
    def __init__(self):
        parser = self.parse_args()

    def init_args(self):
        parser = argparse.ArgumentParser(description='Command Line SBML Modelbuilder')
 #       parser.add_argument('-v', '--version', action='version', version=('%(prog)s ' + VERSION))
        parser.add_argument('-s', '--src', metavar='src', type=str, help='source file name')
        parser.add_argument('-d', '--dst', metavar='dst', type=str, help='output file name')

        return parser

    def parse_args(self):
        args = self.init_args().parse_args()
        args = vars(args)
        self.modelWrapper = ModelWrapper.createModelWrapper(**args)

    def run(self):
        from clsm.myprompt import MyPrompt
        self.prompt = MyPrompt(self.modelWrapper)
        self.prompt.cmdloop()
