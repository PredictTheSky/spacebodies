# -*- coding: utf-8 -*-

"""
tests.utils
~~~~~~~~~~~
A collection of utilities to make testing easier.
"""

import os


def fixture(filename):
    """Locate and return the contents of a JSON fixture."""
    abs_filename = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        filename,
    )

    with open(abs_filename, 'r') as fixture_file:
        return fixture_file.read()
