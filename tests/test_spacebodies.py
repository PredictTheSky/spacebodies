# -*- coding: utf-8 -*-

"""
tests: spacebodies

The test case for SpaceBodies
"""

import unittest

import spacebodies


class SpaceBodiesTestCase(unittest.TestCase):
    def setUp(self):
        self.space_bodies = spacebodies.SpaceBodies()

    def test_next_events(self):
        events = self.space_bodies.next_events("iss", lat=50.7184, lon=-3.5339)

        self.assertEqual(events, [])
