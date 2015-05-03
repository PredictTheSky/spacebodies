# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import httpretty
import os

from utils import fixture

from datetime import datetime
import spacebodies
from spacebodies import forecast

FORECASTIO_API_KEY = os.getenv('FORECAST_KEY', '')
SPACETRACK_USERNAME = os.getenv('SPACETRACK_USERNAME', '')
SPACETRACK_PASSWORD = os.getenv('SPACETRACK_PASSWORD', '')
LATITUDE = "51.47781"
LONGITUDE = "-0.001475"


class SpaceBodiesTestCase(unittest.TestCase):
    def setUp(self):
        self.space_bodies = spacebodies.SpaceBodies(FORECASTIO_API_KEY,
                                                    SPACETRACK_USERNAME,
                                                    SPACETRACK_PASSWORD)

    def register_forecast_http_call(self):
        url = "https://api.forecast.io/forecast/%s/%s,%s"\
              "?units=si&exclude=currently,minutely,daily&extend=hourly" % (
                  FORECASTIO_API_KEY, LATITUDE, LONGITUDE)

        httpretty.register_uri(httpretty.GET, url,
                               body=fixture('forecast.json'))

    def register_spacetrack_http_call(self):
        httpretty.register_uri(httpretty.POST,
                               'https://www.space-track.org/ajaxauth/login',
                               body="")

        url = 'https://www.space-track.org/basicspacedata/query/class/' \
              'tle_latest/NORAD_CAT_ID/25544/ORDINAL/1/'
        httpretty.register_uri(httpretty.GET, url,
                               body=fixture('spacetrack_tle.json'))

    @httpretty.activate
    def test_next_iss_events(self):
        self.register_forecast_http_call()
        self.register_spacetrack_http_call()

        now = datetime(2015, 5, 2, 21, 0, 0)
        events = self.space_bodies.next_events("iss", lat=LATITUDE,
                                               lon=LONGITUDE, timestamp=now)
        """
        Expected results got from Heaven's Above page. Their default
        is the time at 10 degrees above the horizon rather than rise
        time - need to view detail to get rise times. Our results also
        differ by a few seconds, probably due to adjustments for
        horizon and altitude being done by ephem. Heaven's Above also
        reports BST times.
        """
        self.assertGreater(len(events), 0)

    @httpretty.activate
    def test_next_mercury_events(self):
        self.register_forecast_http_call()

        now = datetime(2015, 5, 2, 21, 0, 0)
        events = self.space_bodies.next_events("mercury", lat=LATITUDE,
                                               lon=LONGITUDE, timestamp=now)
        self.assertEqual(len(events), 7)

    @httpretty.activate
    def test_next_venus_events(self):
        self.register_forecast_http_call()

        now = datetime(2015, 5, 2, 21, 0, 0)
        events = self.space_bodies.next_events("venus", lat=LATITUDE,
                                               lon=LONGITUDE, timestamp=now)
        self.assertEqual(len(events), 7)

    @httpretty.activate
    def test_next_mars_events(self):
        self.register_forecast_http_call()

        now = datetime(2015, 5, 2, 21, 0, 0)
        events = self.space_bodies.next_events("mars", lat=LATITUDE,
                                               lon=LONGITUDE, timestamp=now)
        self.assertEqual(len(events), 7)

    @httpretty.activate
    def test_next_jupiter_events(self):
        self.register_forecast_http_call()

        now = datetime(2015, 5, 2, 21, 0, 0)
        events = self.space_bodies.next_events("jupiter", lat=LATITUDE,
                                               lon=LONGITUDE, timestamp=now)
        self.assertEqual(len(events), 7)

    @httpretty.activate
    def test_next_saturn_events(self):
        self.register_forecast_http_call()

        now = datetime(2015, 5, 2, 21, 0, 0)
        events = self.space_bodies.next_events("saturn", lat=LATITUDE,
                                               lon=LONGITUDE, timestamp=now)
        self.assertEqual(len(events), 7)

    @httpretty.activate
    def test_next_uranus_events(self):
        self.register_forecast_http_call()

        now = datetime(2015, 5, 2, 21, 0, 0)
        events = self.space_bodies.next_events("uranus", lat=LATITUDE,
                                               lon=LONGITUDE, timestamp=now)
        self.assertEqual(len(events), 7)

    @httpretty.activate
    def test_next_neptune_events(self):
        self.register_forecast_http_call()

        now = datetime(2015, 5, 2, 21, 0, 0)
        events = self.space_bodies.next_events("neptune", lat=LATITUDE,
                                               lon=LONGITUDE, timestamp=now)
        self.assertEqual(len(events), 7)

    @httpretty.activate
    def test_next_pluto_events(self):
        self.register_forecast_http_call()

        now = datetime(2015, 5, 2, 21, 0, 0)
        events = self.space_bodies.next_events("pluto", lat=LATITUDE,
                                               lon=LONGITUDE, timestamp=now)
        # because the rise time is offset, we'll calculate one short of the
        # others
        self.assertEqual(len(events), 6)

    @httpretty.activate
    def test_next_sirius_events(self):
        self.register_forecast_http_call()

        now = datetime(2015, 5, 2, 21, 0, 0)
        events = self.space_bodies.next_events("sirius", lat=LATITUDE,
                                               lon=LONGITUDE, timestamp=now)
        self.assertEqual(len(events), 7)

    @httpretty.activate
    def test_next_arcturus_events(self):
        self.register_forecast_http_call()

        now = datetime(2015, 5, 2, 21, 0, 0)
        events = self.space_bodies.next_events("arcturus", lat=LATITUDE,
                                               lon=LONGITUDE, timestamp=now)
        self.assertEqual(len(events), 7)

    @httpretty.activate
    def test_next_events_with_default_timestamp(self):
        self.register_forecast_http_call()

        events = self.space_bodies.next_events("mercury", lat=LATITUDE,
                                               lon=LONGITUDE)

        # we're checking that the type responds correctly, but we're not
        # worried about the results
        self.assertIsInstance(events, list)

    def test_next_unknown_star_events(self):
        now = datetime(2015, 5, 2, 21, 0, 0)
        events = self.space_bodies.next_events("unknown_star", lat=LATITUDE,
                                               lon=LONGITUDE, timestamp=now)
        self.assertEqual(events, "There is no such body in catalog")

    @httpretty.activate
    def test_next_events_have_weather(self):
        self.register_forecast_http_call()

        now = datetime(2015, 5, 2, 21, 0, 0)
        events = self.space_bodies.next_events("mars", lat=LATITUDE,
                                               lon=LONGITUDE, timestamp=now)

        for event in events:
            self.assertIn(event.sky_state, forecast.SKY_STATE)


if __name__ == '__main__':
    unittest.main()
