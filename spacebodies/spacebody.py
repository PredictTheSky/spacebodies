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
import ephem
from .forecast import Forecast
from .tle_data import TLE_getter

from .spaceevent import SpaceEvent


class SpaceBody(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, config):
        self._config = config

    def next_events(self, lat, lon, timestamp=None):
        """
        Calculate the next set of space events at a given time
        using the latitude/longitude pair.

        :param lat: Latitude of the location in degrees.
        :param lon: Longitude of the location in degrees.
        :param timestamp: DateTime timestamp. Defaults to now.
        """
        if timestamp is None:
            timestamp = datetime.datetime.now()

        observer = ephem.Observer()
        forecaster = Forecast(self._config.forecast_key)
        forecaster.load(lat, lon)
        observer.lat, observer.lon = lat, lon
        date = ephem.Date(timestamp)
        seven_days_later = date + 6
        if self.category is 'satellite':
            print 'is satellite'
            tle_getter = TLE_getter(self._config.spacetrack_username,
                                    self._config.spacetrack_password)
            self.tle = tle_getter.get_data(self.id)
            print 'tle: %s' % self.tle
            self.body = ephem.readtle(self.tle.tle_line0, self.tle.tle_line1,
                                      self.tle.tle_line2)

        events = []
        while date <= seven_days_later:
            observer.date = date
            self.body.compute(observer)
            """ Avoid overrunning the end date looking for the next event. """
            if self.body.rise_time > seven_days_later:
                break
            if self._is_transit_visible():
                weather = forecaster.forecast(observer.date.datetime())
                events.append(self._next_event(weather.cloud_cover))
            date = self.nudge_date()

        return events

    @abc.abstractmethod
    def nudge_date(self):
        """
        We need to nudge the observer date on a little each time around the
        loop before we look for the next rise/set of the space object. For
        fast moving objects like the ISS we can use the set time and add an
        hour. For planets we just need to check once a day, so we can add
        a day to the rise time.
        """
        pass

    def _is_transit_visible(self):
        return self.body.transit_alt > ephem.degrees("10")

    def _next_event(self, sky_state):
        event = SpaceEvent(self.id, self.name, self.category)
        # TODO: is this correct and useful?
        event.start(self.body.rise_time, (0, self.body.rise_az))
        event.end(self.body.set_time, (0, self.body.set_az))
        event.sky_state(sky_state)

        return event
