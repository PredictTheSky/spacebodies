# -*- coding: utf-8 -*-

"""
bodies
------

This module provides the subclasses of SpaceBody; these are the classes which
handle the calculation for each different type of astronomical object.

See the Abstract Base Class, SpaceBody on the required elements.

"""

import ephem

from .spacebody import SpaceBody


class ISS(SpaceBody):

    def __init__(self):
        """ TLE from Space-Trak, 6th July. """
        self.body = ephem.readtle("ISS (ZARYA)",
            "1 25544U 98067A   13187.51770631  .00005346  00000-0  99606-4 0  1286",
            "2 25544 051.6495 012.5195 0008764 133.4934 272.3907 15.50559659837702")
        self.id = "25544"
        self.name = "International Space Station"
        self.category = "satellite"

    def nudge_date(self):
        return ephem.Date(self.body.set_time + ephem.hour)


class Mars(SpaceBody):

    def __init__(self):
        self.body = ephem.Mars()
        self.id = "mars"
        self.name = "Mars"
        self.category = "planet"

    def nudge_date(self):
        return self.body.rise_time + 1
