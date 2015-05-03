# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from datetime import datetime


class Weather(object):
    """A class to represent the weather at a given point in time."""

    SKY_STATE = ['clear', 'scattered cloud', 'cloudy with breaks', 'cloudy']

    def __init__(self, response):
        self.text_summary = response['summary']
        self.time = datetime.utcfromtimestamp(response['time'])
        self.temperature = response['temperature']
        self.apparent_temperature = response['apparentTemperature']
        self.wind_speed = response['windSpeed']
        self.wind_bearing = response['windBearing']
        self.precipitation_intensity = response['precipIntensity']
        self.precipitation_probability = response['precipProbability']
        self.pressure = response['pressure']
        self.dew_point = response['dewPoint']
        self.humidity = response['humidity']
        self.ozone = response['ozone']
        self.cloud_cover = response['cloudCover']
        self.cloud_summary = self._cloud_to_summary(self.cloud_cover)

    def _cloud_to_summary(self, cloud_cover):
        if cloud_cover < .1:
            return self.SKY_STATE[0]
        if cloud_cover < .4:
            return self.SKY_STATE[1]
        if cloud_cover < .75:
            return self.SKY_STATE[2]
        return self.SKY_STATE[3]

    def __str__(self):
        return "%s (%sºC, feels like: %sºC, sky: %s)" % (
            self.text_summary, self.temperature, self.apparent_temperature,
            self.cloud_summary)
