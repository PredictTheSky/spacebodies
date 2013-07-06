# -*- coding: utf-8 -*-

"""
tests: spacebodies

The test case for SpaceBodies
"""

import datetime
import unittest

import spacebodies


class SpaceBodiesTestCase(unittest.TestCase):
    
    def setUp(self):
        self.space_bodies = spacebodies.SpaceBodies()

    def test_next_events(self):
        test_timestamp = datetime.datetime(2013, 7, 6, 0, 0)
        events = self.space_bodies.next_events("iss", lat="50.7184",
            lon="-3.5339", timestamp=test_timestamp)
        """
        Expected results got from Heaven's Above page. Their default
        is the time at 10 degrees above the horizon rather than rise
        time - need to view detail to get rise times. Our results also
        differ by a few seconds, probably due to adjustments for
        horizon and altitude being done by ephem. Heaven's Above also
        reports BST times.
        """
        self.assertEqual(len(events), 48)
        self.assertEqual("2013/7/6 09:19:39", str(events[0].start))
        self.assertEqual("2013/7/15 11:39:01", str(events[-1].start))
        

if __name__ == '__main__':
    unittest.main()
