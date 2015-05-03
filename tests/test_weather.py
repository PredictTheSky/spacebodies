#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import json

from utils import fixture

from spacebodies import forecast


class WeatherTestCase(unittest.TestCase):
    def test_builds_object_from_forecast_response(self):
        forecast_response = json.loads(fixture('forecast_response.json'))

        weather = forecast.Weather(forecast_response)

        self.assertEqual(weather.text_summary, forecast_response['summary'])
        self.assertEqual(weather.temperature, forecast_response['temperature'])
        self.assertEqual(weather.cloud_cover, forecast_response['cloudCover'])

    def test_generates_cloud_summary(self):
        forecast_response = json.loads(fixture('forecast_response.json'))

        weather = forecast.Weather(forecast_response)

        self.assertEqual(weather.cloud_summary, 'cloudy with breaks')

if __name__ == '__main__':
    unittest.main()
