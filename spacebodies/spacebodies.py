# -*- coding: utf-8 -*-

"""
spacebodies.spacebodies
-----------------------

This module provides the public interface to the library.

"""

import datetime
import bodies


class SpaceBodies(object):
    """The public interface to the library."""
    ERROR_NO_BODY = "There is no such body in catalog"

    def __init__(self):
        self.spacebodies = {
            'iss': bodies.ISS(),
            'mercury': bodies.Mercury(),
            'venus': bodies.Venus(),
            'mars': bodies.Mars(),
            'jupiter': bodies.Jupiter(),
            'saturn': bodies.Saturn(),
            'uranus': bodies.Uranus(),
            'neptune': bodies.Neptune(),
            'pluto': bodies.Pluto(),
        }
        for k, v in bodies.STAR_CATALOG.iteritems():
            self.spacebodies[v['id']] = bodies.Star(v['name'])

    def next_events(self, body, lat, lon, timestamp=datetime.datetime.now):
        """
        Get the next events for a given space body, location and time.

        :param body: The astronomical body. As a string, e.g.: "iss".
        :param lat: Latitude of the location in degrees.
        :param lon: Longitude of the location in degrees.
        :param timestamp: DateTime timestamp. Defaults to now.
        """
        try:
            spacebody = self.spacebodies[body]
            return spacebody.next_events(lat, lon, timestamp)
        except KeyError:
            return self.ERROR_NO_BODY