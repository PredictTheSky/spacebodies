# -*- coding: utf-8 -*-

"""
spacebodies.spacebody
---------------------

This module provides the Abstract Base Class which is used for implementing
space bodies in the library. You should subclass this to add more bodies/
event types.

"""

import abc
import datetime


class SpaceBody(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def next_events(self, lat, lon, timestamp=datetime.datetime.now):
        """
        Calculate the next set of space events at a given time
        using the latitude/longitude pair.

        :param lat: Latitude of the location in degrees.
        :param lon: Longitude of the location in degrees.
        :param timestamp: DateTime timestamp. Defaults to now.
        """
        return
