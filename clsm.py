#! /opt/local/bin/python
# -*- coding: utf-8 -*-

import argparse
from modelWrapper import *
from myPrompt import *

__version__ = '1.0.0'

def main():
    parser = argparse.ArgumentParser(description='Command Line SBML Modelbuilder')
    parser.add_argument('-v', '--version', action='version', version=('%(prog)s ' + __version__))
    parser.add_argument('-s', '--src', metavar='src', type=str, help='source file name')
    parser.add_argument('-d', '--dst', metavar='dst', type=str, help='output file name')

    args = vars(parser.parse_args())
    modelwrapper = modelWrapper.createModelWrapper(**args)

    prompt = myPrompt()
    prompt.cmdloop()

if __name__ == '__main__':
    main()
