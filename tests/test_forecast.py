# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import httpretty
import os

from utils import fixture

from datetime import datetime
from spacebodies import forecast

FORECASTIO_API_KEY = os.getenv('FORECAST_KEY', '')
LATITUDE = 51.585278
LONGITUDE = -0.078056


class ForecastTestCase(unittest.TestCase):
    def setUp(self):
        self.forecaster = forecast.Forecast(FORECASTIO_API_KEY)

    def register_forecast_http_call(self):
        url = "https://api.forecast.io/forecast/%s/%s,%s"\
              "?units=si&exclude=currently,minutely,daily&extend=hourly" % (
                  FORECASTIO_API_KEY, LATITUDE, LONGITUDE)

        httpretty.register_uri(httpretty.GET, url,
                               body=fixture('forecast.json'))

    @httpretty.activate
    def test_loads_forecast(self):
        self.register_forecast_http_call()

        self.forecaster.load(LATITUDE, LONGITUDE)

        self.assertNotEqual(self.forecaster._cached_weather_events, {})

    @httpretty.activate
    def test_returns_forecast_for_datetime(self):
        self.register_forecast_http_call()

        self.forecaster.load(LATITUDE, LONGITUDE)

        # time at the point the fixture was fetched
        now = datetime(2015, 5, 2, 21, 9, 0)
        weather = self.forecaster.forecast(now)

        # assert the response object behaves right
        self.assertIsNotNone(weather)
        self.assertIsInstance(weather, forecast.Weather)

        # the time returned should be rounded up
        self.assertEqual(weather.time, datetime(2015, 5, 2, 21, 0, 0))

    @httpretty.activate
    def test_throws_exception_when_out_of_range(self):
        self.register_forecast_http_call()

        self.forecaster.load(LATITUDE, LONGITUDE)

        with self.assertRaises(forecast.ForecastOutOfRangeError):
            now = datetime(2015, 4, 26)
            self.forecaster.forecast(now)

    def test_throws_exception_when_out_of_order(self):
        with self.assertRaises(forecast.ForecastNotLoadedError):
            now = datetime(2015, 4, 27, 16, 57, 00)
            self.forecaster.forecast(now)

if __name__ == '__main__':
    unittest.main()
