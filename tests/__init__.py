# -*- coding: utf-8 -*-

"""
tests
-----

This subpackage contains the tests for spacebodies.

Each module is split into a different file.

"""

import os.path
import unittest


def get_tests():
    """Grab all of the tests to provide them to setup.py"""
    start_dir = os.path.dirname(__file__)
    return unittest.TestLoader().discover(start_dir, pattern='*.py')
