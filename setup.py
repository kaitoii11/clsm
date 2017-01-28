#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from clsm import __author__, __version__, __license__

setup(
        name = 'clsm',
        version = __version__,
        description = 'Command Line SBML Modelbuilder',
        license = __license__,
        autho = __author__,
        packages = find_packages(),
        )
