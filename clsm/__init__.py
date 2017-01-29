#!/usr/bin/env python
# coding: utf-8

__author__  = 'Kaito Ii'
__version__ = '0.0.1'
__license__ = 'MIT'

from clsm.main import clsmMain

def main():
#   global clsm
   clsm = clsmMain()
   clsm.run()
