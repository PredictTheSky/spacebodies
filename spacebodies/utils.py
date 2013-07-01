# -*- coding: utf-8 -*-

"""
spaceobjects.utils
------------------

This module provides utility functions that the library uses that might be
useful elsewhere. It's mostly for plugin loading.

"""

import imp
import os


def load_subclass(subclass):
    """
    Loads the given subclass and makes it available.

    :param subclass: a subclass reference
    """
    return


def find_subclasses(path, cls):
    """
    Finds and calls :func:`load_subclass` on classes specified
    in the path specified. This is the main plugin code.

    :param path: the path to search
    :param cls: the class to find
    """
    return
