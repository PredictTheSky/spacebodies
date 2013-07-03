# -*- coding: utf-8 -*-

"""
bodies
------

This module provides the subclasses of SpaceBody; these are the classes which
handle the calculation for each different type of astronomical object.

See the Abstract Base Class, SpaceBody on the required elements.

"""

import datetime

from .spacebody import SpaceBody


class ISS(SpaceBody):
    def next_events(self, lat, lon, timestamp=datetime.datetime.now):
        return []
