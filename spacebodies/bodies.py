# -*- coding: utf-8 -*-

"""
bodies
------

This module provides the subclasses of SpaceBody; these are the classes which
handle the calculation for each different type of astronomical object.

See the Abstract Base Class, SpaceBody on the required elements.

"""

import datetime
import ephem

from .spacebody import SpaceBody
from .spaceevent import SpaceEvent


class ISS(SpaceBody):

    def __init__(self):
        """ TLE from Space-Trak, 6th July. """
        self.body = ephem.readtle("ISS (ZARYA)",
            "1 25544U 98067A   13187.51770631  .00005346  00000-0  99606-4 0  1286",
            "2 25544 051.6495 012.5195 0008764 133.4934 272.3907 15.50559659837702")
        self.id = "25544"
        self.name = "International Space Station"
        self.category = "satellite"


    def next_events(self, lat, lon, timestamp=datetime.datetime.utcnow()):
        observer = ephem.Observer()
        observer.lat, observer.lon = lat, lon

        date = ephem.Date(timestamp)
        ten_days_later = date + 10
        events = []
        while date <= ten_days_later:
            observer.date = date
            self.body.compute(observer)
            """ Avoid overrunning the end date looking for the next event. """
            if self.body.rise_time > ten_days_later:
                break
            if self._is_transit_visible():
                events.append(self._next_event())            
            date = ephem.Date(self.body.set_time + ephem.hour)
        return events
    

    def _is_transit_visible(self):
        return self.body.transit_alt > ephem.degrees("10")

    def _next_event(self):
        event = SpaceEvent(self.id, self.name, self.category)
        event.start(self.body.rise_time, (0, self.body.rise_az))
        event.end(self.body.set_time, (0, self.body.set_az))
        return event
