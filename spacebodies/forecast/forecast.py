# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from datetime import datetime, timedelta
import requests

from .exceptions import ForecastNotLoadedError, ForecastOutOfRangeError
from .weather import Weather


class Forecast(object):
    """
    A class for fetching hourly forecasts for the coming week.
    The full week is cached to make repeating requests fast.
    """
    FORECASTIO_ENDPOINT = 'https://api.forecast.io/forecast'
    FORECASTIO_ARGS = 'units=si&exclude=currently,minutely,daily&extend=hourly'

    def __init__(self, api_key=""):
        self._api_key = api_key
        self._cached_weather_events = {}  # a cache using datetimes as keys

    def load(self, lat, lon):
        """Load a 7 day Forecast for a given location."""
        # empty the cache
        self._cached_weather_events = {}

        # TODO: check if api_key is blank, if so, throw config error

        # load in new events
        r = requests.get("%s/%s/%s,%s?%s" % (self.FORECASTIO_ENDPOINT,
                                             self._api_key,
                                             lat, lon,
                                             self.FORECASTIO_ARGS))

        # fill the cache with Weather objects
        data = r.json()
        hourly = data["hourly"]
        for hour in hourly["data"]:
            weather = Weather(hour)
            self._cached_weather_events[weather.time] = weather

    def forecast(self, datetime):
        """Fetch the forecast for a given datetime."""
        if self._cached_weather_events == {}:
            raise ForecastNotLoadedError("You must load the forecast before \
                                            requesting it.")

        nearest_hour = self._nearest_hour(datetime)

        try:
            return self._cached_weather_events[nearest_hour]
        except Exception, e:
            raise ForecastOutOfRangeError(e)

    def _nearest_hour(self, dt):
        """Determine the nearest full hour."""
        cutoff = datetime(dt.year, dt.month, dt.day, 23, 30)
        if dt >= cutoff:
            # jump forward to tomorrow at midnight
            return datetime(dt.year, dt.month, dt.day, 0, 0) + timedelta(1)
        if dt.minute >= 30:
            return datetime(dt.year, dt.month, dt.day, dt.hour, 0) + \
                timedelta(hours=1)

        return datetime(dt.year, dt.month, dt.day, dt.hour, 0)
