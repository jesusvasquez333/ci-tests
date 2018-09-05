#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(name='maths',
      version='1.0',
      description='Math function library',
      author='Jesu Vasquez',
      packages=find_packages('src'),
      package_dir={'': 'src'}
      )
