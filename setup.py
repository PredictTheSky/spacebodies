#!/usr/bin/env python

import os
import sys

import spacebodies

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = ['spacebodies']

requires = []

setup(
    name='spacebodies',
    version=spacebodies.__version__,
    description='Space Objects combined with Weather Data',
    long_description=open('README.rst').read() + '\n\n' +
    open('HISTORY.rst').read(),
    author='Nick Charlton',
    author_email='info@predictthesky.org',
    url='http://predictthesky.org/',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'spacebodies': 'spacebodies'},
    include_package_data=True,
    install_requires=requires,
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(),
)
