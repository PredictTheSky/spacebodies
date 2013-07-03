# -*- coding: utf-8 -*-

"""
spacebodies.spacebodies
-----------------------

This module provides the public interface to the library.

"""

import datetime

from bodies import ISS


class SpaceBodies(object):
    """The public interface to the library."""
    def __init__(self):
        self.bodies = {'iss': ISS}

    def next_events(self, body, lat, lon, timestamp=datetime.datetime.now):
        """
        Get the next events for a given space body, location and time.

        :param body: The astronomical body. As a string, e.g.: "iss".
        :param lat: Latitude of the location in degrees.
        :param lon: Longitude of the location in degrees.
        :param timestamp: DateTime timestamp. Defaults to now.
        """
        action = self.bodies[body]()
        return action.next_events(lat, lon, timestamp)
