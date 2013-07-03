#!/usr/bin/env python

import os
import sys
from setuptools import setup

import spacebodies

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

install_requires = []

setup(
    name='spacebodies',
    version=spacebodies.__version__,
    description='Space Objects combined with Weather Data',
    long_description='\n\n'.join([
        open('README.rst').read(),
        open('HISTORY.rst').read()
    ]),
    license=open('LICENSE').read(),
    author='Nick Charlton',
    author_email='info@predictthesky.org',
    url='http://predictthesky.org/',
    packages=['spacebodies'],
    package_data={'': ['LICENSE']},
    package_dir={'spacebodies': 'spacebodies'},
    install_requires=install_requires,
    zip_safe=False,
    test_suite="tests.get_tests"
)
