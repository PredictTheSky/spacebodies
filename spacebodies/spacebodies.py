# -*- coding: utf-8 -*-

"""
spacebodies.spacebodies
-----------------------

This module provides the public interface to the library.

"""

import datetime
import bodies


class Config(object):
    def __init__(self):
        self.forecast_key = ''
        self.spacetrack_username = ''
        self.spacetrack_password = ''


class SpaceBodies(object):
    """The public interface to the library."""
    ERROR_NO_BODY = "There is no such body in catalog"

    def __init__(self, forecast_key='', spacetrack_username='',
                 spacetrack_password=''):
        self._config = Config()
        self._config.forecast_key = forecast_key
        self._config.spacetrack_username = spacetrack_username
        self._config.spacetrack_password = spacetrack_password

        self.spacebodies = {
            'iss': bodies.ISS(self._config),
            'mercury': bodies.Mercury(self._config),
            'venus': bodies.Venus(self._config),
            'mars': bodies.Mars(self._config),
            'jupiter': bodies.Jupiter(self._config),
            'saturn': bodies.Saturn(self._config),
            'uranus': bodies.Uranus(self._config),
            'neptune': bodies.Neptune(self._config),
            'pluto': bodies.Pluto(self._config),
        }
        for k, v in bodies.STAR_CATALOG.iteritems():
            self.spacebodies[v['id']] = bodies.Star(self._config, v['name'])

    def next_events(self, body, lat, lon, timestamp=None):
        """
        Get the next events for a given space body, location and time.

        :param body: The astronomical body. As a string, e.g.: "iss".
        :param lat: Latitude of the location in degrees.
        :param lon: Longitude of the location in degrees.
        :param timestamp: DateTime timestamp. Defaults to now.
        """
        if timestamp is None:
            timestamp = datetime.datetime.now()

        try:
            spacebody = self.spacebodies[body]
            return spacebody.next_events(lat, lon, timestamp)
        except KeyError:
            return self.ERROR_NO_BODY
